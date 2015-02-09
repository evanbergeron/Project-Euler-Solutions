def isPrime(n):
    if n == 2: return True
    if n < 2: return False
    if n % 2 == 0: return False
    maxFactor = int(round(n**.5))
    for i in xrange(3, maxFactor + 1, 2):
        if n % i == 0: return False
    return True

def makePrimes():
    num = 2
    while True:
        if isPrime(num):
            yield num
        num += 1

def isSumOfConsecPrimes(n):

