import math

def f30():
    n = 3
    summation = 0
    while True:
        if isFact(n): 
            print "n:", n
            summation += n
            print "sum:", summation
        n += 1


def isFact(n):
    digits = [int(char) for char in str(n)]
    summation = 0
    for digit in digits: summation += math.factorial(digit)
    return n == summation

f30()
