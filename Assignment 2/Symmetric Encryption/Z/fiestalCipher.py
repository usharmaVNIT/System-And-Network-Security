# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


def function(block , key):
    newBlock = []
    for e in block:
        newBlock.append(e^key)
    return newBlock


def xorBlocks(block1 , block2):
    block = []
    for e1,e2 in zip(block1,block2):
        block.append(e1^e2)
    return block


def fistalRoundEncrypt(plainText , key):
    length = len(plainText)//2
    left = plainText[:length]
    right = plainText[length:]
    newLeft = [ord(x) for x in left]
    newRight = [ord(x) for x in right]
    func = function(newRight , key)
    xor = xorBlocks(newLeft , func)
    left = ''.join([chr(x) for x in newRight])
    right = ''.join([chr(x) for x in xor])
    return left+right
  
def fistalCipherEncrypt(plainText ,  numberOfRounds , keys):
  if len(plainText)%2 !=0:
    plainText+='$'
    odd = True

    # 0010 -> 2 , 0001 -> 1 => 00100001 => (21)hex (8 bits) = (33)dec = key1
    # 00010101 -> 21 in dec
    # block contains 8 bit numbers

  # Encryption
  for i in range(numberOfRounds):
    plainText = fistalRoundEncrypt(plainText , keys[i])
    print("encrypted Text of round %d : "%(i+1),plainText)
  return plainText


    
def fistalRoundDecrypt(cipherText , key):
  length = len(cipherText)//2
  left = cipherText[:length]
  right = cipherText[length:]
  newLeft = [ord(x) for x in left]
  newRight = [ord(x) for x in right]

  func = function(newLeft , key)
  xor = xorBlocks(newRight , func)

  left = ''.join([chr(x) for x in xor])
  right = ''.join([chr(x) for x in newLeft])
  return left+right

def fistalCipherDecrypt(cipherText , numberOfRounds , keys):
  # Decryption
  for i in range(numberOfRounds):
    cipherText = fistalRoundDecrypt(cipherText , keys[len(keys)-1-i])
    print("decrypted Text of round %d : "%(i+1),cipherText)
  
  return cipherText







def getKeys():
  keys : list
  with open('keys.txt' , 'r') as f:
    keys = list(map(int  , f.readline().strip().split(',')))
  print("Keys : " , keys)
  return keys




# def fistalCipher(plainText , numberOfRounds = 2):
#   odd = False
#   if len(plainText)%2 !=0:
#     plainText+='$'
#     odd = True


#     # 0010 -> 2 , 0001 -> 1 => 00100001 => (21)hex (8 bits) = (33)dec = key1
#     # 00010101 -> 21 in dec
#     # block contains 8 bit numbers
#   keys = [33 , 21]
#   # Encryption
#   for i in range(numberOfRounds):
#     plainText = fistalRoundEncrypt(plainText , keys[i])
#     print("encrypted Text of round %d : "%(i+1),plainText)

#   print("\nencrypted Text : ",plainText)
#   print('\n')
  
#   # Decryption
#   for i in range(numberOfRounds):
#     plainText = fistalRoundDecrypt(plainText , keys[len(keys)-1-i])
#     print("decrypted Text of round %d : "%(i+1),plainText)

#   if odd==True:
#     plainText = plainText[:-1]
  
#   print("\ndecrypted Text :" , plainText)
#   print('\n')
#   return plainText

# a = "This is question 1-Z of SNS Assignment 2"
# print("Orignal Text : " , a)
# fistalCipher(a , 2)
