# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import socket
from random import randint
from utils import *



sender = 'Alice'
senderKey  : str


def getKey(name):
    global senderKey
    with open('keys.txt' , 'r') as f:
        lines = f.readlines()
        for line in lines:
            pname , pkey = line.strip().split(':')
            if pname == name:
                senderKey = pkey
                break
    


def getRecieverKey(reciever , KDCAddress):
    global sender
    global senderKey
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.connect(KDCAddress)
        RA = randint(100 , 100000)
        data = '==-->'.join([sender , reciever , str(RA) ])
        print("\tsending data : " , data)
        sock.send(data.encode('utf-16'))
        data = sock.recv(1024).decode('utf-16')
        RA , reciever , tempKey , ticketRecieverEncrypted = decrypt(data , senderKey).split('==-->')
        print('\tRecieved key : %s and token : %s'%(tempKey , ticketRecieverEncrypted))
        print("********************************************************************************")
        print("********************************************************************************")
        return tempKey , ticketRecieverEncrypted



def connect(reciever , recieverAddress , KDCAddress):
    global senderKey
    getKey(sender)
    tempKey , ticketRecieverEncrypted = getRecieverKey(reciever , KDCAddress)
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.connect(recieverAddress)
        print("Sending the ticket to Bob")
        sock.send(ticketRecieverEncrypted.encode('utf-16'))
        data = sock.recv(1024).decode('utf-16').strip()
        print("Recieved RB : %s , decrypting ... "%data)
        RB = decrypt(data , tempKey)
        token = int(RB) - 1
        print("Sending RB-1 : %d after encryption"%token)
        token = encrypt(str(token) , tempKey)
        sock.send(token.encode('utf-16'))
        verified = sock.recv(1024).decode('utf-16').strip()
        if verified == "Verified":
            print("********************************************************************************")
            print("********************************************************************************")
            print("Secured Connection established ..")
            while True:
                data = input("Send Something : ")
                data = encrypt(data , tempKey)
                print("Encrypted Data : " , data)
                sock.send(data.encode('utf-16'))
                print("Waiting For Response")
                data = sock.recv(1024)
                if not data:
                    print("Connection Closed")
                    break
                data = data.decode('utf-16')
                print("Encrypted Data Recieved : ", data)
                data = decrypt(data , tempKey)
                print("Decrypted Data : " , data)





def main():
    KDCAddress = ('localhost' , 5000)
    reciever="Bob"
    recieverAddess = ('localhost' , 5002)
    connect(reciever , recieverAddess , KDCAddress)

if __name__ == '__main__':
    main()


