# Roy Basmacier 24813
# Samuel Lee 24774
import random
import warnings
import string
import sympy
from Crypto.Hash import SHA3_256


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


def random_prime(bitsize):
    warnings.simplefilter('ignore')
    chck = False
    while chck == False:
        p = random.randrange(2**(bitsize-1), 2**(bitsize)-1)
        chck = sympy.isprime(p)
    warnings.simplefilter('default')
    return p


def large_DL_Prime(q, bitsize):
    warnings.simplefilter('ignore')
    chck = False
    while chck == False:
        k = random.randrange(2**(bitsize-1), 2**bitsize-1)
        p = k*q+1
        chck = sympy.isprime(p)
    warnings.simplefilter('default')
    return p


def Public_Parameter_Generator(qsize, psize):
    q = random_prime(qsize)
    p = large_DL_Prime(q, psize-qsize)
    tmp = (p-1)//q
    g = 1
    while g == 1:
        alpha = random.randrange(1, p)
        g = pow(alpha, tmp, p)
    return q, p, g


def KeyGen(q, p, g):
  alpha = random.randrange(1, q-2) # 0 < a < q-1
  beta = pow(g, alpha, p)
  return alpha, beta


def SignGen(message, q, p, g, a):
    h_obj = SHA3_256.new(message)
    # h_obj.update(int.from_bytes(message, byteorder='big'))
    h = int.from_bytes(h_obj.digest(), byteorder='big') % q
    k = random.randrange(1, q-2)
    r = pow(g, k, p) % q
    s = (a * r - k * h) % q
    return s, r


def SignVer(message, s, r, q, p, g, beta):
    h_obj = SHA3_256.new(message)
    # h_obj.update(int.from_bytes(message, byteorder='big'))
    h = int.from_bytes(h_obj.digest(), byteorder='big') % q # divide by 8?
    v = modinv(h, q)
    z1 = (s * v) % q
    z2 = (r * v) % q
    u = ((pow(modinv(g, p),z1,p) * pow(beta,z2,p))% p) % q
    if u == r:
        return False # check this part
    else:
        return True


def random_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    s = ''
    for i in range(length):
      s += random.choice(password_characters)
    return s


def GenerateOrRead(filename):
  try:
    with open(filename, 'r') as file:
      q = int(file.readline())
      p = int(file.readline())
      g = int(file.readline())
  except:
    with open('pubparams.txt', 'w') as file:
      q, p, g = Public_Parameter_Generator(224,2048)
      file.write(str(q) + '\n')
      file.write(str(p) + '\n')
      file.write(str(g) + '\n')
  return q, p, g
