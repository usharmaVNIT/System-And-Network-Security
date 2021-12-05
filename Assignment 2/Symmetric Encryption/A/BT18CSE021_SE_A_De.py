# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import socket
from DES import DES

host = 'localhost'
port = 4000

IV = 'QUES-1-A'


def xorBlock(block1 , block2):
    newBlock1 = [ord(x) for x in block1]
    newBlock2 = [ord(x) for x in block2]
    block = []
    for e1,e2 in zip(newBlock1 , newBlock2):
        block.append(e1^e2)
    return block



address = (host , port)
def main():
    des = DES()
    key : str
    with open('key.txt' , 'r') as keyFile:
        key = keyFile.readline().strip()

    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.bind(address)
        sock.listen()
        while True:
            print("Server Listining ...")
            print("Server Address -> %s:%d"%(host , port))
            client , addr = sock.accept()
            with client:
                print("Connected to : " , addr)
                print("Sending Initial Vector ...")
                clientIV= IV
                client.send(IV.encode())
                print("Sent IV : ", clientIV)
                while True:
                    data = client.recv(18)
                    if not data:
                        break
                    data = data.decode('utf-16')[:8]
                    print('\t' , "Encrypted Message Recieved = ", data)
                    decrypted = des.decrypt(key , data)
                    decrypted = xorBlock(decrypted , clientIV)
                    decrypted = ''.join([chr(x) for x in decrypted])
                    print('\t' , "Message Decrypted : ", decrypted)
                    clientIV = data



if __name__ == "__main__":
    main()