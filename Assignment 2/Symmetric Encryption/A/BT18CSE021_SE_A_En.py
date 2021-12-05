# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import socket
from DES import DES


IV : str

def createBlocks(plainText):
    blocks = []
    for i in range(0 , len(plainText) , 8):
        blocks.append(plainText[i:i+8])
    if len(blocks[-1])<8:
        block = blocks[-1]
        while len(block)%8 !=0:
            block+='$'
        blocks[-1]=block
    return blocks




def xorBlock(block1 , block2):
    newBlock1 = [ord(x) for x in block1]
    newBlock2 = [ord(x) for x in block2]
    block = []
    for e1,e2 in zip(newBlock1 , newBlock2):
        block.append(e1^e2)
    return block



def sendToServer(address):
    des = DES()
    key : str
    with open('key.txt' , 'r') as keyFile:
        key = keyFile.readline().strip()
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.connect(address)
        IV = sock.recv(10).decode()
        print("Recieved IV :" , IV)
        while True:
            plainText = input("Input the text that you want to send (will be broken into blocks of 8) :\n")
            blocks = createBlocks(plainText)
            for block in blocks:
                blockAscii = xorBlock(block , IV)
                blockText = ''.join([chr(x) for x in blockAscii])
                encrypted = des.encrypt(key , blockText)
                sock.send(encrypted.encode('utf-16'))
                print("Sent encrypted Text %s ( %s ) " %(encrypted , block))
                IV = encrypted

def main():
    host = 'localhost'
    port = 4000
    address = (host , port)
    sendToServer(address)

if __name__ == "__main__":
    main()





