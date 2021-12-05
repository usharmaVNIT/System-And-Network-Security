import sys

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




def main():
    argv = sys.argv
    a = int(argv[1])
    ans = PHI(a)
    print(*ans , len(ans) , end='')


if __name__ == "__main__":
    main()
