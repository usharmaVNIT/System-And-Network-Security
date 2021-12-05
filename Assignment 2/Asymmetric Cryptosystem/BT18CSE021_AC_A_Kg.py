# Ujjwal Sharma
# BT18CSE021
# usharma@students.vnit.ac.in


from random import choice

def getPrimes():
    primesList = []
    with open('primes.txt' , 'r') as f:
        for line in f.readlines():
            primes = list(map(int , line.strip().split()))
            primesList.extend(primes)
    return primesList

primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]



def savePrimeList():
    primes = getPrimes()
    with open('primesList.txt' , 'w') as f:
        f.write(str(primes))
    print('done')


# Python program to demonstrate working of extended
# Euclidean Algorithm
	
# function for extended Euclidean Algorithm
def gcdExtended(a, b):

	# Base Case
	if a == 0 :
		return b, 0, 1
			
	gcd, x1, y1 = gcdExtended(b%a, a)
	
	# Update x and y using results of recursive
	# call
	x = y1 - (b//a) * x1
	y = x1
	
	return gcd, x, y
	

def keyGen():
    # primes = getPrimes()
    global primes
    p = choice(primes)
    q = choice(primes)
    while p == q:
        q = choice(primes)
    n = p*q
    phi = (p-1)*(q-1)
    e = choice(primes)
    while (e>=phi) or (phi%e == 0):
        e = choice(primes)
    gcd , d , tmp = gcdExtended(e , phi)
    d%=phi
    publicKey = (e , n)
    privateKey = d
    with open('RSA-Key.txt' , 'w') as f:
        f.write('n , e , d\n')
        f.write(str(n) + ',' + str(e) + ',' + str(d)+'\n')
        f.write('Public Key = (e , n)\nPrivate Key = d\n') 
    return publicKey , privateKey

print(keyGen())
     
    
    
