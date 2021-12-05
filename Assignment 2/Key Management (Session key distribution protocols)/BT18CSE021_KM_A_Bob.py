# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import socket
from random import randint
from utils import *


reciever = 'Bob'
recieverKey : str


host= 'localhost'
port = 5002
address = (host , port) 

def getKey(name):
    global recieverKey
    with open('keys.txt' , 'r') as f:
        lines = f.readlines()
        for line in lines:
            pname , pkey = line.strip().split(':')
            if pname == name:
                recieverKey = pkey
                break
    


def server():
    global reciever
    global recieverKey
    global address
    getKey(reciever)
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.bind(address)
        sock.listen()
        while True:
            print("%s's server listining ( waiting for sessionKey ) "%reciever)
            print("%s's Address -> %s:%d"%(reciever ,host , port))
            client , addr = sock.accept()
            with client:
                print("Connected to : " , addr)
                data = client.recv(1024)
                if not data:
                    continue
                data = data.decode('utf-16')
                print("Encoded Data recieved : " , data)
                data = decrypt(data , recieverKey)
                print("Decrypted Data : " , data)
                sender , tempKey = data.strip().split('==-->')
                RB = randint(10**15 , 10**30)
                data = encrypt(str(RB) , tempKey)
                print("sending RB : %d , encrypted : %s"%(RB , data))
                client.send(data.encode('utf-16'))
                data = client.recv(1024).decode('utf-16').strip()
                print("recieved encrypted RB-1 " , data)
                data = decrypt(data , tempKey)
                RBVal = int(data)
                if RBVal == RB-1:
                    client.send("Verified".encode('utf-16'))
                    print("********************************************************************************")
                    print("********************************************************************************")
                    print("Secured Connection Is established")
                    while True:
                        data = client.recv(1024)
                        if not data:
                            break
                        data = data.decode('utf-16')
                        print("Encrypted Data : " , data)
                        data = decrypt(data , tempKey)
                        print("Decrypted Data : " , data)
                        data = input("Send Something : ")
                        data = encrypt(data , tempKey)
                        print("Encrypted Data : " , data)
                        client.send(data.encode('utf-16'))


def main():
    server()

if __name__ == '__main__':
    main()
