import random
import sys
from ecpy.curves import Curve
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


def KeyGen(E):
    n = E.order
    sA = random.randint(0, n - 2)
    P = E.generator
    QA = sA * P
    # TODO: check if QA is on the curve
    #(Q.y * Q.y) % p == (Q.x ** 3 + a * Q.x + b) % p
    return sA, QA # sA, QA -> secret key, public key


def SignGen(message, E, sA):
    n = E.order
    P = E.generator
    h_obj = SHA3_256.new(message)
    h = int.from_bytes(h_obj.digest(), byteorder='big') % n
    k = random.randint(1, n - 2)
    R = k * P
    r = R.x % n
    s = ((sA * r) - (k * h )) % n
    return s, r


def SignVer(message, s, r, E, QA): # returns 0 if valid 1 if non valid
    #-z1 *P +z2*Q
    #n-z1
    n = E.order
    P = E.generator
    h_obj = SHA3_256.new(message)
    h = int.from_bytes(h_obj.digest(), byteorder='big') % n
    v = modinv(h, n)
    z_1 = (s * v) % n
    z_2 = (r * v) % n
    u = ((QA * z_2) - (P * z_1))
    if (u.x % n) == (r % n):
        return False
    else:
        return True

