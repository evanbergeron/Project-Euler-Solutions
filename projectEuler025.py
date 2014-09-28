def fib(numOfDigits):
    fibs = [1,1]
    count = 2
    while len(str(fibs[1])) < numOfDigits:
        nextFib = sum(fibs)
        fibs[0] = fibs[1]
        fibs[1] = nextFib
        count += 1
        print count, fibs[1]

    return count

print fib(1000)
