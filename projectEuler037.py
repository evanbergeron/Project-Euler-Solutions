def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    maxFactor = int(round(n**0.5))
    for i in xrange(3, maxFactor + 1, 2):
        if n % i == 0: return False
    return True

def isTruncPrime(n):
    return isTruncLeftPrime(n) and isTruncRightPrime(n)

def isTruncLeftPrime(n):
    n = str(n)
    for i in xrange(1, len(n)):
        if not isPrime(int(n[i:])):
            return False
    return True

def isTruncRightPrime(n):
    n = str(n)
    for i in xrange(1, len(n)):
        if not isPrime(int(n[:i])):
            return False
    return True

def f37():
    summ = 0
    n = 8
    while True:
        if isPrime(n) and isTruncPrime(n):
            summ += n
            print n, summ
        n += 1

f37()
