def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    maxFactor = int(n**0.5)
    for div in xrange(3, maxFactor + 1, 2):
        if n % div == 0:
            return False
    return True


def primesGen():
    n = 2
    while True:
        if not isPrime(n):
            n += 1
        yield n


