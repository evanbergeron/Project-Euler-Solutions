def isPalindrome(string): return string == string[::-1]
def f36():
    summ = 0
    n = 1
    for n in xrange(1, 1000000):
        #print bin(n)[2:]
        if isPalindrome(str(n)) and isPalindrome(bin(n)[2:]):
            summ += n
            print summ

f36()
