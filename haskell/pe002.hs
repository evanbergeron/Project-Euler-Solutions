fib :: Int -> Int
fib 0 = 1
fib 1 = 2
fib n = fib (n-1) + fib (n-2)

fourMil = 4000000
ans = sum (takeWhile (<= fourMil) (filter even [fib n | n <- [1..]]))

-- Second shot, now with lazy lists
fibs = 1 : 2 : zipWith (+) fibs (tail fibs)
ans2 = sum (takeWhile (< fourMil) (filter even fibs))
