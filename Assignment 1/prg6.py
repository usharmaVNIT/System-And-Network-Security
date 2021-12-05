import sys

# function for extended Euclidean Algorithm
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
    a , m = int(argv[1]) , int(argv[2])
    gcd , x , y = GCDExtended(a , m)
    if gcd != 1:
        print("N" , end='')
        return
    print('Y' , x%m , end='') 
    # print(' %s * %s + %s * %s = %s ' % (x , a, y , m , gcd))


if __name__ == "__main__":
    main()

