def f30():
    n = 2
    summation = 0
    while True:
        if isPower(n, 5): 
            print "n:", n
            summation += n
            print "sum:", summation
        n += 1


def isPower(n, power):
    digits = [int(char) for char in str(n)]
    summation = 0
    for digit in digits: summation += digit**power
    return n == summation

f30()
