def isEvenDiv20(n):
    for i in xrange(2, 21):
        if (n % i != 0): return False
    return True

n = 20

while True:
    if isEvenDiv20(n): 
        print n
        break
    n += 20
