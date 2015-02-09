def f29(aUpper, bUpper):
    nums = set()
    for i in xrange(2, aUpper + 1):
        for j in xrange(2, bUpper + 1):
            nums.add(i**j)
            nums.add(j**i)
    return len(nums)

print f29(100,100)
