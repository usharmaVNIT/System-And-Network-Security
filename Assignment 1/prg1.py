import sys


def GCD(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    return GCD(b , a%b)

def divisors(a):
    ans = []
    i = 1
    while i<=a:
        if a%i == 0:
            ans.append(i)
        i+=1
    return ans


def main():
    argv = sys.argv
    count = argv[1]
    numbers = list(map(int , argv[2:]))
    if len(numbers)<2:
        ans = divisors
        print(*ans)
        return
    gcd = GCD(numbers[0] , numbers[1])
    for e in numbers[2:]:
        gcd = GCD(e , gcd)
    ans = divisors(gcd)
    print(*ans , end='')



if __name__ == "__main__":
    main()
