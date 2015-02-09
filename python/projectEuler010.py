def sieve(n):
    primes = [True]*(n+1)
    primes[0] = primes[1] = False
    total = 2
    for i in xrange(3,n+1,2):
        if primes[i]:
            print i, "is prime."
            total += i
            for j in xrange(2*i, n+1, i):
                print j, "isn't."
                primes[j] = False
    return total

print sieve(2000000)
