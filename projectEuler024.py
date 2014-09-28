import itertools
count = 0
for _ in itertools.permutations("0123456789", 10):
    count += 1
    if count == 1000000: print count, _
