# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


import socket
from random import randint



def verify(sock , publicKey , n):
    x = int(sock.recv(1024).decode())
    print("recieved x : " , x)
    c = randint(0,1)
    print("sending challenge : " , c)
    sock.send(str(c).encode())
    y = int(sock.recv(1024).decode())
    print("recieved y : %d, checking "%y)
    ySQ = y**2 %n 
    xvc = x*(publicKey**c) %n
    if ySQ == xvc:
        print("Verified")
        sock.send("Verified".encode())
        return True
    print("Not Verified")
    sock.send("Cannot Verify .. Check your key".encode())
    return False 


def main():
    with open('keys.txt' , 'r') as f:
        lines = f.readlines()
        n , _ , publicKey = list(map(int , lines[-1].strip().split(',')))
    
    host = 'localhost'
    port = 4000
    address = (host , port)

    with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as sock:
        sock.bind(address)
        sock.listen()
        while True:
            print("Server Listining ...")
            print("Server Address -> %s:%d"%(host , port))
            client , addr = sock.accept()
            with client:
                print("Connected to : " , addr)
                print("Verifying ...")
                numberOfRounds = 6
                print("Number of verifying rounds : " , numberOfRounds)
                client.send(str(numberOfRounds).encode())
                verified = True
                rounds = 0
                while (rounds<numberOfRounds) and (verified == True):
                    print("************* Round Number *************** :          " , rounds+1)
                    verifiedLoop = verify(client , publicKey , n)
                    verified&=verifiedLoop
                    rounds+=1
                
                if verified== False:
                    client.close()
                    continue
                while True:
                    data = client.recv(1024)
                    if not data:
                        break
                    data = data.decode()
                    print('\t' , "Message Recieved = ", data)


if __name__ == "__main__":
    main()