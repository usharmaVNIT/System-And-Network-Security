import sys


def order(a , m):
    i = 1
    p = (a)%m
    while p%m != 1:
        p = (p*a)%m
        i+=1
    return i

def main():
    argv = sys.argv
    a , m = int(argv[1]) , int(argv[2])
    print(order(a , m) , end='')


if __name__ == "__main__":
    main()
