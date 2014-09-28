def isPyTriple(a,b,c): return a**2 + b**2 == c**2

def f10(n):
    for i in xrange(2, 1000):
        for j in xrange(i, 1000-i):
            k = 1000 - i - j                
            if isPyTriple(i, j, k) and i + j + k == 1000:
                return i*j*k
            print i, j, k, i+j+k

print f10(1)
