# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import socket
from RSA import *

host = 'localhost'
port = 5000
address = (host , port)

def server():
    publicKey , privateKey , N = getKey()
    global address
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.bind(address)
        sock.listen()
        while True:
            print("Server listining ... ")
            print("Server's Address -> %s:%d"%(host , port))
            client , addr = sock.accept()
            with client:
                print("Connected to : " , addr)
                while True:
                    print("Waiting ... ")
                    data = client.recv(1024)
                    if not data:
                        break
                    data = data.decode('utf-16')
                    encrypted , paddedLength = data.split(':')
                    paddedLength = int(paddedLength)
                    encrypted = list(map(int , encrypted.split(',')))
                    print("\tEncoded Data recieved ---> ")
                    print('\t\t' , *encrypted)
                    print("\tdecrypting ...")
                    decrypted = OAEPDecrypt(encrypted , privateKey , N , paddedLength)
                    print("\tDecrypted Data ------->> ")
                    print('\t\t' , decrypted)
                    client.send('ok'.encode())


def main():
    server()


if __name__ == "__main__":
    main()