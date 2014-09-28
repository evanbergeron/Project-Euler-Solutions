import time
start = time.time()
print sum([int(char) for char in str(2**1000)])
print time.time() - start
