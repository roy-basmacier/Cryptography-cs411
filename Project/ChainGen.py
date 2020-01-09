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


def AddBlock2Chain(PoWLen, TxCnt, block_candidate, PrevBlock):
    if PrevBlock == '':
        PrevPoW = '00000000000000000000'
    else:
        PrevPoW = PrevBlock[-2][14:-1]
        nonce = int(PrevBlock[-1][7:-1])
        leaves = []
        for i in range(TxCnt):
            leaves.append(''.join(PrevBlock[9 * i:9 * i + 9]).encode('UTF-8'))
        root = getRoot(leaves)
        digest = root + PrevPoW.encode('UTF-8') + nonce.to_bytes((nonce.bit_length() + 7)// 8, byteorder='big')
        h_obj = SHA3_256.new(digest)
        PrevPoW = h_obj.hexdigest()
        if PrevPoW[:PoWLen] != '0' * PoWLen:
            return ''



    leaves = []
    transactions = []
    for i in range(TxCnt):
        leaves.append(''.join(block_candidate[9*i:9*i+9]).encode('UTF-8'))
        transactions.append(''.join(block_candidate[9*i:9*i+9]))


    root = getRoot(leaves)
    nonce = random.getrandbits(128)
    digest = root + PrevPoW.encode('UTF-8') + nonce.to_bytes((nonce.bit_length()+7)//8, byteorder='big')
    h_obj = SHA3_256.new(digest)
    hexdigest = h_obj.hexdigest()
    while hexdigest[:PoWLen] != '0' * PoWLen:
        nonce = random.getrandbits(128)
        digest = root + PrevPoW.encode('UTF-8') + nonce.to_bytes((nonce.bit_length() + 7) // 8, byteorder='big')
        h_obj = SHA3_256.new(digest)
        hexdigest = h_obj.hexdigest()

    # 1 generate a random nonce
    # 2 check if the hash of new block (with nonce) has PowLen of zeros infront)
    # 3 go to 1 until 2 is valid
    # 4 write and return
    # check powlen

    NewBlock = ''.join(transactions) + 'Previous PoW: ' + PrevPoW + '\nNonce: ' + str(nonce) + '\n'
    return NewBlock, PrevPoW

