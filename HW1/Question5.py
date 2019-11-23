'''

    5.Decrypt the following plaintext using Vigènere cipher where the secret key is "SANITY":
    "A RRNNQW TB IGQOEE BAYL QHMLRAOA WG RZE TZHSFDF BAYL I QWG’R CNBE MFW AAAPCJ. "s

    Note that only the letter characters are encrypted.

'''
from hw01_helper import *
cipherText = "A RRNNQW TB IGQOEE BAYL QHMLRAOA WG RZE TZHSFDF BAYL I QWG’R CNBE MFW AAAPCJ."
key = "SANITY"

# we assume that the key is always in uppercase format
def Vigenere_Dec(ctext, key):
    ptext = ''
    # We will iterate i over the key and we will do so multiple times
    i = 0
    for ch in ctext:
        # Since this is decipher algorithm we will subtract the cipher text's letter from the key's ith letter mod 26
        if ch in uppercase:
            ptext += inv_uppercase[(uppercase[ch] - uppercase[key[i]]) % 26]
            i += 1
        elif ch in lowercase:
            ptext += inv_lowercase[(lowercase[ch] - uppercase[key[i]]) % 26]
            i += 1
        else:
            ptext += ch
        i %= len(key)
    return ptext


print(Vigenere_Dec(cipherText, key))
# What is the plain text?
# I REFUSE TO ANSWER THAT QUESTION ON THE GROUNDS THAT I DON’T KNOW THE ANSWER.
''' :D '''
