def encrypt(plainText , key):
    plainTextAscii = [ord(x) for x in plainText]
    key = [ord(x) for x in key]
    keyLen = len(key)
    block = []
    i , j = 0 , 0
    while i<len(plainTextAscii):
        value = plainTextAscii[i]^key[j]
        i+=1
        j = (j+1)%keyLen
        block.append(value)
    block = ''.join([chr(x) for x in block])
    return block

def decrypt(cipherText , key):
    cipherTextAscii = [ord(x) for x in cipherText]
    key = [ord(x) for x in key]
    keyLen = len(key)
    block = []
    i , j = 0 , 0
    while i<len(cipherTextAscii):
        value = cipherTextAscii[i]^key[j]
        i+=1
        j = (j+1)%keyLen
        block.append(value)
    block = ''.join([chr(x) for x in block])
    return block
