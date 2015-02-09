# From lecture notes online 
def isPrime(n): 
    if (n < 2): return False 
    if (n == 2): return True 
    if (n % 2 == 0): return False 
    maxFactor = int(round(n**0.5)) 
    for factor in xrange(3,maxFactor+1,2): 
        if (n % factor == 0):  
            return False 
    return True 

# From lecture notes online 
def nthPrime(n): 
    found = 0 
    guess = 0 
    while (found < n): 
        guess += 1 
        if (isPrime(guess)): 
            found += 1
            print "The %dth prime is %d" % (found, guess)
    return guess 

print nthPrime(10001)
