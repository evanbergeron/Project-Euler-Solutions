# def lexigraphicallyOrdered

def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    maxFactor = int(round(n ** 0.5))
    for posFactor in xrange(3, maxFactor + 1, 2):
        if n % posFactor == 0:
            return False
    return True

def primes():
    guess = 2
    while True:
        if isPrime(guess):
            yield guess
        guess += 1

def primeFactorization(n, divisors):
    if n == 1 or n == 0: return divisors
    if n == 0: return False
    allPrimes = primes()
    currPrime = next(allPrimes)
    while currPrime <= n ** 0.5:
        if n % currPrime == 0:
            divisors.append(currPrime)
            result = primeFactorization(n / currPrime, divisors)
            if result:
                return result
        currPrime = next(allPrimes)

print primeFactorization(4, [])
