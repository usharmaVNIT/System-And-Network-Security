# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import hashlib
from random import randint
from hashlib import md5


blockLength = 16
k = blockLength//2

def hashFunction(block):
    hashed = md5(block.encode()).hexdigest()
    return hashed



def encryptRSA(block , publicKey):
    blockAscii = [ord(x) for x in block]
    encryptedBlock = []
    e , n = publicKey
    for char in blockAscii:
        value = char**e%n
        encryptedBlock.append(value)
    return encryptedBlock


def decryptRSA(encryptedBlockAscii , privateKey , n):
    decryptedBlock = []
    for e in encryptedBlockAscii:
        value = e**privateKey%n
        decryptedBlock.append(value)
    decrypted = ''.join([chr(x) for x in decryptedBlock])
    return decrypted

def getKey():
    n : int
    e : int
    d : int
    with open('RSA-Key.txt' , 'r') as file:
        lines = file.readlines()
        n , e , d = list(map(int , lines[1].strip().split(',')))
    
    publicKey = (e , n)
    privateKey = d
    return publicKey ,privateKey , n


def xorBlocks(block1 , block2):
    block1Ascii = [ord(x) for x in block1]
    block2Ascii = [ord(x) for x in block2]
    i , j = 0 , 0
    block = []
    while i<len(block1Ascii) and j<len(block2Ascii):
        block.append(block1Ascii[i]^block2Ascii[j])
        i+=1
        j+=1
    while i<len(block1Ascii):
        block.append(block1Ascii[i])
        i+=1
    while j<len(block2Ascii):
        block.append(block2Ascii[j])
        j+=1
    block = ''.join([chr(x) for x in block])
    return block


def generateRChars(r):
    A = ord('A')
    z = ord('z')
    rChars = ''
    for _ in range(r):
        val = chr(randint(A , z))
        rChars+=val
    return rChars

def generateGChars(kChars , m):
    l = len(kChars)
    i = 0
    gChars = ''
    while i<m:
        gChars+=kChars[i%l]
        i+=1
    return gChars


def OAEPEncrypt(block , publicKey):
    global blockLength
    global k
    paddedLength = 0
    while len(block) < blockLength:
        block+='$'
        paddedLength+=1
    kChars = generateRChars(k)
    mChars = generateGChars(kChars , blockLength)
    M = xorBlocks(block , mChars)
    hashValue = str(hashFunction(M))[:k]
    xorHash = xorBlocks(hashValue , kChars)
    newPlainText = M+xorHash
    cipherText = encryptRSA(newPlainText , publicKey)
    return cipherText , paddedLength

def OAEPDecrypt(encryptedBlockAscii , privateKey , n , paddedLength):
    global k
    newPlainText = decryptRSA(encryptedBlockAscii , privateKey , n)
    P1 = newPlainText[:-k]
    P2 = newPlainText[-k:]
    hashValue = str(hashFunction(P1))[:k]
    kChars = xorBlocks(hashValue , P2)
    gChars = generateGChars(kChars , blockLength)
    M = xorBlocks(P1 , gChars)

    return M[:-paddedLength]





    



# a = 'RSA Working'
# print("Getting KEY")
# pk, d , n = getKey()
# print('n :%d , pk : %d , pkd : %d'%(pk[1] , pk[0] , d))
# print("encrypting -> ", a , '...')
# enc = encryptRSA(a , pk)
# print("Encrypted ----->>> :" , *enc)
# print()
# print('decrypting ...')
# dec = decryptRSA(enc , d , n)
# print('\ndecrypted ------->>> ' , dec)



# print("Using OAEP")


# print("encrypting -> ", a , '...')
# enc , pl = OAEPEncrypt(a , pk)
# print("Encrypted ----->>> :" , *enc)
# print()
# print('decrypting ...')
# dec = OAEPDecrypt(enc , d , n , pl)
# print('decrypted ------->>> ' , dec)






