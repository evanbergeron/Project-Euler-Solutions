digits 0 = []
digits n = n `mod` 10 : digits (n `div` 10)
isPalindrome n = (digits n) == reverse (digits n)
threeProds = [x*y | x <- [999, 998..100], y <- [999, 998..100]]
ans = maximum [x | x <- threeProds, isPalindrome x]
