import time
starttime = time.time()

def genCollatz(n):
    seed = n
    count = 0
    while n != 1:
        n = n / 2 if (n % 2 ==0) else 3*n + 1
        count += 1
        # print seed, n
        #if n == 1: print "%d got to 1 in %d steps" % (seed, count)
        yield n

def f14(upper):
    num = 1
    maxCount = 0
    maxCountNum = 0
    for i in xrange(3,upper):
        count = 0
        for _ in genCollatz(i): count += 1
        if count > maxCount:
            maxCount = count
            maxCountNum = i
            print "New maxCount is %d with %d steps" % (maxCountNum, maxCount)
        #if count >= 1000000: print i, count
    return maxCountNum

endtime = time.time() - starttime
print f14(1000000)
print endtime
