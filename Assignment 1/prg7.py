import sys


def GCDExtended(a, b):
    if a == 0 : 
        return b, 0, 1
            
    gcd, x1, y1 = GCDExtended(b%a, a)
    
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
    
    return gcd, x, y


def main():
    argv = sys.argv
    a , b , m = int(argv[1]) , int(argv[2]) , int(argv[3])
    gcd , _ , _ = GCDExtended(a , m)
    if b%gcd != 0:
        print('N')
        return
    alpha , mue = a // gcd , m // gcd
    beta = b //gcd

    ngcd , alphaInv , mueInv = GCDExtended(alpha , mue)

    k = 0
    solutions = []
    while k<gcd:
        solution = alphaInv*beta + k*mue
        solutions.append(solution % m)
        k+=1

    solutions.sort()
    if len(solutions)>0:
        print('Y' , len(solutions) , *solutions , end='')
    else:
        print('N' , end='')





if __name__ == "__main__":
    main()
