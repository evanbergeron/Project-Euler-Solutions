def isPalindrome(string): return string == string[::-1]
prod3Digs = [i*j for i in xrange(999, 0, -1) for j in xrange(999, 0, -1) if isPalindrome(str(i*j))]
print sorted(prod3Digs)[-1]
