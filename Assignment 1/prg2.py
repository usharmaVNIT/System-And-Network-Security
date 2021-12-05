import sys

# function for extended Euclidean Algorithm
def GCDExtended(a, b):
    if a == 0 : 
        return b, 0, 1
            
    gcd, x1, y1 = GCDExtended(b%a, a)
    
    x = y1 - (b//a) * x1
    y = x1
    
    return gcd, x, y
     

def main():
    argv = sys.argv
    a , b = int(argv[1]) , int(argv[2])
    gcd , x , y = GCDExtended(a , b)
    print(*[x, y] , end='')


if __name__ == "__main__":
    main()



