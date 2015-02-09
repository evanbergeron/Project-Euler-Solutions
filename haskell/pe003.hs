isPrimeHelper n 1 = True
isPrimeHelper n d = if (n `mod` d == 0) then False else isPrimeHelper n (d-1)

isPrime n = isPrimeHelper n (n-1)
primes = [x | x <- [1..], isPrime x]

factors n = [factor | factor <- [2..n-1], n `mod` factor == 0 && isPrime factor]

-- Final approach
maxFactor :: Int -> Int -> Int
maxFactor n d = if (n `mod` d == 0 && n `div` d == 1) then d
                else if (n `mod` d == 0) then maxFactor (n `div` d) (d)
                else maxFactor n (d + 1)

ans = maxFactor 600851475143 2
