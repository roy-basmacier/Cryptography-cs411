'''
    1. Consider the shift cipher.
    Show that the ciphertext “NZWO” can be decrypted into two meaningful English words.
    Find out those words and the corresponding encryption keys.
'''
from hw01_helper import *

# I will use brute force to find the 2 words it could correspond to
cipherText = 'NZWO'
shiftedTexts = []  # a list of all the possible words along with the key

for i in range(26):
    shiftedText = ''
    for ch in cipherText:
        # shift each character by i also take the modules of 26 so it loops around the alphabet
        shiftedText += inv_uppercase[(uppercase[ch] + i) % 26]
    shiftedTexts.append((shiftedText, i))
print(shiftedTexts)
# We get the following:
# [('NZWO', 0), ('OAXP', 1), ('PBYQ', 2), ('QCZR', 3), ('RDAS', 4), ('SEBT', 5), ('TFCU', 6), ('UGDV', 7), ('VHEW', 8),
# ('WIFX', 9), ('XJGY', 10), ('YKHZ', 11), ('ZLIA', 12), ('AMJB', 13), ('BNKC', 14), ('COLD', 15), ('DPME', 16),
# ('EQNF', 17), ('FROG', 18), ('GSPH', 19), ('HTQI', 20), ('IURJ', 21), ('JVSK', 22), ('KWTL', 23), ('LXUM', 24),
# ('MYVN', 25)]

# From the result we can conclude that the possible words can be either COLD or FROG with the keys 15 or 18 respectively
