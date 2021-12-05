import sys
import math



def getPrimes(n):
      
    ans = []
    while n % 2 == 0:
        ans.append(2)
        n = n//2
          
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i == 0:
            ans.append(i)
            n = n//i
    if n > 2:
        ans.append(n)
    return ans

def main():
    argv = sys.argv
    a = int(argv[1])
    ans = getPrimes(a)
    print(*ans,end='')

if __name__ == "__main__":
    main()



