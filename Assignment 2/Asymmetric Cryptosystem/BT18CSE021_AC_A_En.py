# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import socket
from RSA import *

def send(address):
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.connect(address)
        # getting Public Key
        publicKey, _ , N = getKey()
        while True:
            data = input('Enter Something (length <= %d ) : '%blockLength)
            if len(data) > 16:
                data = data[:16]
            print("Encrypting ...")
            encryption , paddedLength = OAEPEncrypt(data , publicKey)
            print("Encrypted ----> ")
            print('\t' , *encryption)
            value = ','.join([str(x) for x in encryption])
            sendingData = ':'.join([value , str(paddedLength)])
            sock.send(sendingData.encode('utf-16'))
            print("Waiting for response .. ")
            resp = sock.recv(1024)
            print("acknowledged ..")
        

def main():
    host = 'localhost'
    port = 5000
    address = (host , port)
    send(address)

if __name__ == "__main__":
    main()

