import sys
from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def GCD(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    return GCD(b , a%b)


def getPrimes(n):
      
    ans = []
    while n % 2 == 0:
        ans.append(2)
        n = n//2
          
    for i in range(3, int(sqrt(n))+1, 2):
        while n%i == 0:
            ans.append(i)
            n = n//i
    if n > 2:
        ans.append(n)
    return set(ans)




def PHIModified(n):
    primes = getPrimes(n)
    num = n
    for e in primes:
        num*=(e-1)
    for e in primes:
        num//=e
    return num
    

       


def fermatTheorem(a , x , n , phi):
    quo = x%phi
    exp = a**quo
    retVal = exp%n
    return retVal

def fermat(a , x , n):
    if isPrime(n):
        return fermatTheorem(a , x , n , n-1)
    else:
        phi = PHIModified(n)
        return fermatTheorem(a , x , n , phi)

def main():
    argv = sys.argv
    a , x , n = int(argv[1]) , int(argv[2]) , int(argv[3])
    if x == 0:
        print(1 , end='')
        return
    if GCD(a , n)==1:
        print(fermat(a , x , n) , end='')
        return
    binRep = list(map(int , bin(x)[2:]))[::-1]
    b = 1
    A = a
    if binRep[0] == 1:
        b = a
    for i in range(1 , len(binRep)):
        A = (A*A)%n
        # print(A)
        if binRep[i]==1:
            b = (A*b)%n
    print(b , end='')

    

if __name__ == "__main__":
    main()
    


