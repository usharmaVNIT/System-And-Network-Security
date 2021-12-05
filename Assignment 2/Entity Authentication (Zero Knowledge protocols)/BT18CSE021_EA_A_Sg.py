# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import socket
from random import randint


def getKeys():
    with open('keys.txt' , 'r') as f:
        lines = f.readlines()
        n , secretKey , publicKey = list(map(int , lines[-1].strip().split(',')))
    return n , secretKey , publicKey


def claim(sock , privateKey , n):
    print("generating r")
    r = randint(1 ,n-1)
    print("r : " , r)
    print("Generating witness")
    x = r**2 %n # Witness
    print("witness : " , x)
    print("sending Witness")
    sock.send(str(x).encode())
    c = int(sock.recv(1024).decode()) # challenge
    print("challenge Recieved : " , c)
    y = r*(privateKey**c) %n
    print('y : ' , y)
    print("Sending y")
    sock.send(str(y).encode())
    response = sock.recv(1024).decode()
    if response == 'Verified':
        print("Claimed")
        return True
    print(response)
    return False


def communicate(address):
    n , privateKey , publicKey = getKeys()
    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.connect(address)
        numberOfRounds = int(sock.recv(1024).decode())
        print("Number Of rounds : " , numberOfRounds)
        claimed = True
        rounds = 0
        while (rounds<numberOfRounds) and (claimed==True):
            print("************* Round Number *************** :          " , rounds+1)
            claimed = claimed&claim(sock , privateKey , n)
            rounds+=1
        
        if claimed == True:
            while True:
                data = input("Enter what you need to send : \n")
                sock.send(data.encode())


def main():
    host= 'localhost'
    port = 4000
    address = (host , port)
    communicate(address)

if __name__ == "__main__":
    main()

