'''
    3. Assume that you design a new affine cipher where you encrypt two letters at a time, where your alphabet is
    In other words, you group your plaintext message in bigrams(i.e., two-character words)
    and encrypt each bigram of the plaintext separately using this affine cipher.
    If the number of letters in the plaintext is not a multiple of two, you pad it with the letter “X”.
    Determine the modulus and the size of the key space.

    {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10,
     'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20,
      'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25, ' ':26, '.':27, ',': 28, '!': 29, '?':30}.

'''
from hw01_helper import *
'''
    Since we have 31 characters in our language and we want to encrypt two letters at a time,
    we will calculate the possible combinations of each character which is 31x31 = 961
    x and y ∈ Z961
    Key: k = (α, β) and α, β ∈ Z961
    Encryption: Ek(x) = y = α · x + β mod 961
    Decryption: Dk(x) = x = α^−1 · y + γ mod 961
    Key Space:
    β can be any number in Z961.
    gcd(α, 961) = 1 → α ∈ A → len(A) = phi(961) = 930
    The key space has 961 · 930 = 893730.


'''
print(phi(961) * 961)