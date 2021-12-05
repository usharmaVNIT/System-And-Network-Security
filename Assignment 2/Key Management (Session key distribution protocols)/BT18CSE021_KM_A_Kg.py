# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


from random import randint


def generateKey(n):
    A = ord('A')
    z = ord('z')
    rChars = ''
    for _ in range(n):
        val = chr(randint(A , z))
        rChars+=val
    return rChars


def generateKeys(names):
    n = 15
    with open('keys.txt' , 'w') as f:
        for name in names:
            key = generateKey(n)
            f.write(name+':'+key+'\n')


def main():
    names = ["Alice" , "Bob"]
    generateKeys(names)


if __name__ == "__main__":
    main()

