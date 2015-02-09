isPrime' n 1 = True
isPrime' n d = (n `mod` d /= 0) && isPrime' n (d-1)
isPrime n = isPrime' n (n - 1)
-- primes = [x | x <- [2..], isPrime x]
-- ans = last (take 10001 primes)

-- sieve x = x : [y | y <- [x..], y `mod` x /= 0]

sieve n soFarSoGood = let first = if soFarSoGood n then [n] else [] in
                      first ++ sieve (n + 1) (\x -> soFarSoGood x && x `mod` n /= 0)

primes = sieve 2 (\x -> True)

ans = take 10001 primes
