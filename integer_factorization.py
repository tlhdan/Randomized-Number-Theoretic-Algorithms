import random
from greatest_common_divisor import euclid
from primality_testing import miller_rabin
from collections import Counter

def pollard_rho(n, c=1):
    i = 1
    x = random.randint(0, n - 1)
    y = x
    k = 2
    for _ in range(int(n ** 0.5)):
        i += 1
        x = (x ** 2 - c) % n
        d = euclid(y - x, n)

        if d == n:
            c = random.randint(1, n - 1)
            while c != 2:
                c = random.randint(1, n - 1)
            return pollard_rho(n, c)
        
        if d != 1:
            return d
        
        if i == k:
            y = x
            k *= 2

def factorize(n):
    if n == 1:
        return Counter({1:1})
    
    def helper(n):
        result = Counter({})

        if miller_rabin(n):
            result[n] += 1
            return result
        
        d = pollard_rho(n)
        result += helper(d)
        result += helper(n // d)

        return result
    
    pow_of_2 = 0
    while n % 2 == 0:
        pow_of_2 += 1
        n //= 2

    pow_of_3 = 0
    while n % 3 == 0:
        pow_of_3 += 1
        n //= 3
    
    result = Counter({})
    if pow_of_2 > 0:
        result[2] = pow_of_2
    if pow_of_3 > 0:
        result[3] = pow_of_3
    if n != 1:
        result += helper(n)
    
    return result