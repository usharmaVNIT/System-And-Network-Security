# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import socket

from fiestalCipher import *


def connect(address):
    keys = getKeys()
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            data = input("Enter any text : ")
            encrypt = fistalCipherEncrypt(data , 2 , keys)
            print("encrypted :" , encrypt)
            sock.send(encrypt.encode('utf-16'))
            data = sock.recv(1024).decode('utf-16')
            print('Acknowledged')

def main():
    host = 'localhost'
    port = 4000
    address = (host , port)
    connect(address)


if __name__ == "__main__":
    main()



