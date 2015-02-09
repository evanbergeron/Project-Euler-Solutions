factorial 0 = 1
factorial n = n * factorial (n - 1)

choose n k = if k < 0 || k > n then 0 else
             factorial n `div` (factorial k * factorial (n-k))
