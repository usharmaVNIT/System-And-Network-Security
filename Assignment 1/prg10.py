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


def order(a , m):
    i = 2
    p = (a*a)%m
    while p%m != 1:
        p = (p*a)%m
        i+=1
    return i


def getPrimitiveRoots(m):
    phi = PHI(m)
    primitiveRoots = []
    for root in phi:
        if order(root , m) == len(phi):
            primitiveRoots.append(root)
    return primitiveRoots


def main():
    argv = sys.argv
    m = int(argv[1])
    primitiveRoots = getPrimitiveRoots(m)
    print(len(primitiveRoots) , *primitiveRoots , end='')

if __name__ == "__main__":
    main()