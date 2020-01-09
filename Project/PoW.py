from Crypto.Hash import SHA3_256
import random


def getRoot(leaves):
    if len(leaves) == 1:
        h_obj = SHA3_256.new(leaves[0])
        return h_obj.digest()

    newLeaves = []
    for i in range(0, len(leaves), 2):
        left = leaves[i]
        right = leaves[i + 1]
        h_obj_left = SHA3_256.new(left)
        h_obj_right = SHA3_256.new(right)
        newDigest = h_obj_left.digest() + h_obj_right.digest()
        newLeaves.append(newDigest)
    return getRoot(newLeaves)


def CheckPow(p, q, g, PoWLen, TxCnt, filename):
    with open(filename, 'r') as file:
        leaves = []
        i = 0
        transaction = ''
        nonce = ''
        for line in file:
            if 'Nonce' in line:
                nonce += line[7:]
            transaction += line
            i += 1
            if i == 7:
                leaves.append(transaction.encode('UTF-8'))
                i = 0
                transaction = ''
        print(leaves)
        if len(leaves) > 0:
            # CALCULATE ROOT
            root = getRoot(leaves)
            digest = root + (str(nonce)).encode('UTF-8')
            h_obj = SHA3_256.new(digest)
            hexdigest = h_obj.hexdigest()
            if hexdigest[:PoWLen] == '0' * PoWLen:
                return hexdigest
            return ''
        return line


def PoW(PoWLen, q, p, g, TxCnt, filename):
    with open(filename, 'r') as file:
        leaves = []
        i = 0
        transaction = ''
        for line in file:
            transaction += line
            i += 1
            if i == 7:
                leaves.append(transaction.encode('UTF-8'))
                i = 0
                transaction = ''

        # CALCULATE ROOT
        root = getRoot(leaves)
        nonce = random.getrandbits(128)

        digest = root + (str(nonce)).encode('UTF-8')
        h_obj = SHA3_256.new(digest)
        hexdigest = h_obj.hexdigest()
        while hexdigest[:PoWLen] != '0' * PoWLen:
            nonce = random.getrandbits(128)
            digest = root + (str(nonce)).encode('UTF-8')
            h_obj = SHA3_256.new(digest)
            hexdigest = h_obj.hexdigest()
        with open(filename, 'r') as file1:
            block = file1.read()
            block += 'Nonce: ' + str(nonce)
        return block
