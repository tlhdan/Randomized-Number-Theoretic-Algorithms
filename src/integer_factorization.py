import random
from src.greatest_common_divisor import euclid as gcd
from src.primality_testing import is_prime
from collections import Counter

def pollard_rho(n, c_random=True, c=-1):
    while True:
        i = 1
        x = random.randint(0, n - 1)
        y = x
        k = 2
        if c_random:
            c = random.randint(1, n - 1)

        for _ in range(int(5 * n ** 0.25)):
            i += 1
            x = (x ** 2 + c) % n
            d = gcd(y - x, n)

            if d != 1 and d != n:
                return d
            
            if i == k:
                y = x
                k *= 2

def factorize(n):
    result = Counter({})

    if is_prime(n):
        result[n] += 1
        return result
    
    d = pollard_rho(n)
    result += factorize(d)
    result += factorize(n // d)

    return result