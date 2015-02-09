def generateTriangularNumbers():
    n = 1
    while True:
        yield n*(n+1) / 2
        n += 1

triNums = generateTriangularNumbers()

def countDivisors(n):
    numDivs = 0
    maxFactor = int(round(n**0.5))
    for i in xrange(1, maxFactor + 1):
        if (n % i == 0): numDivs += 1
        if i**2 == n: return 2*numDivs - 1
    return numDivs*2

def f11(n):
    result = next(triNums)
    while countDivisors(result) < n:
        result = next(triNums)
        print result, countDivisors(result)
    return result

print f11(500)
