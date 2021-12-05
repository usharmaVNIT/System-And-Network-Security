# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import socket
from random import randint
from utils import *

keys = {}

host= 'localhost'
port = 5000
address = (host , port)

def getKeys():
    global keys
    with open('keys.txt' , 'r') as f:
        for line in f.readlines():
            entity , entityKey = line.strip().split(':')
            keys[entity] = entityKey



def generateTemporaryKey(lower , upper):
    tempKey = ''
    A = ord('A')
    z = ord('z')
    for _ in range(lower):
        char = randint(A , z)
        tempKey+=chr(char)
    limit = randint(0,upper-lower)
    for _ in range(limit):
        char = randint(A , z)
        tempKey+=chr(char)
    return tempKey



    




def server():
    getKeys()
    global address
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.bind(address)
        sock.listen()
        while True:
            print("Key Distribution Center(KDC) Server Listining ...")
            print("Server Address -> %s:%d"%(host , port))
            client , addr = sock.accept()
            with client:
                print("Connected to : " , addr)
                data = client.recv(1024)
                if not data:
                    continue
                data = data.decode('utf-16')
                print('\t' , data)
                sender , reciever , RA = data.strip().split('==-->')
                senderKey = keys[sender]
                recieverKey = keys[reciever]
                tempKey = generateTemporaryKey(5,10)
                ticketReciever = '==-->'.join([reciever , tempKey])
                ticketRecieverEncrypted = encrypt(ticketReciever , recieverKey)
                ticketSender = '==-->'.join([RA , reciever , tempKey , ticketRecieverEncrypted])
                print('\t' , 'Sender Ticket : ' , ticketSender)
                ticketSenderEncrypted = encrypt(ticketSender , senderKey)
                client.send(ticketSenderEncrypted.encode('utf-16'))
                print("Sent")
                print("********************************************************************************")
                print("********************************************************************************")


def main():
    server()

if __name__ == '__main__':
    main()







    