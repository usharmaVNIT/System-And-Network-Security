import sys
from math import sqrt



def GCD(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    return GCD(b , a%b)

def PHI(a):
    ans = []
    for i in range(1 , a):
        if GCD(i , a) == 1:
            ans.append(i)
    return ans



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
    


def GCDExtended(a, b):
    if a == 0 : 
        return b, 0, 1
            
    gcd, x1, y1 = GCDExtended(b%a, a)
    
    x = y1 - (b//a) * x1
    y = x1
    
    return gcd, x, y
     


def CRT(numbers):
    for i in range(len(numbers)):
        g = GCD(numbers[i][0] , numbers[i][2])
        if numbers[i][1]%g != 0:
            return False , float('inf') , "Cannot solve Linear Congruence for :-  %sx = %s modulo(%s)" %(numbers[i][0] , numbers[i][1] , numbers[i][2])
        numbers[i][0]//=g
        numbers[i][1]//=g
        numbers[i][2]//=g
    for i in range(len(numbers)):
        for j in range(i+1 , len(numbers)):
            if GCD(numbers[i][2] , numbers[j][2]) != 1 :
                return False , float('inf') , "Not Co-Prime :-  %s , %s" %(numbers[i][2] , numbers[j][2])

    newNumbers = []
    for e in numbers:
        if e[0]==1:
            newNumbers.append(e)
        else:
            phi = PHIModified(e[2])
            exp = phi-1
            inverse = e[0] ** exp
            bi = (e[1]*inverse) % e[2]
            newNumbers.append([1 , bi , e[2]])

    M = 1
    for num in newNumbers:
        M*=num[2]
    ans = 0
    # print(newNumbers)
    for num in newNumbers:
        mj = num[2]
        aj = num[1]
        Mbymj = M//mj
        gcd , bj , kk = GCDExtended(Mbymj , mj)
        # print(" %sx%s(mby) + %sx%s(mj) = %s" %(bj , Mbymj , kk , mj , gcd))
        ans += (Mbymj*bj * aj)

    ans = ans%M
    return True , ans , 'The solution to the congruences is of the form x = %s + %sK where k is any integer' %(ans , M)





def main():
    argv = sys.argv

    i = 2
    numbers = []
    while i<len(argv):
        lst = list(map(int , argv[i:i+3]))
        numbers.append(lst)
        i+=3
    ans = CRT(numbers)
    if ans[0]==False:
        print('N' , end='')
    else:
        print('Y' , ans[1] , end='')


if __name__=="__main__":
    main()