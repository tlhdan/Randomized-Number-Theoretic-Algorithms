import random
from greatest_common_divisor import euclid

def pollard_rho(n):
    i = 1
    x = random.randint(0, n - 1)
    y = x
    k = 2
    while True:
        i += 1
        x = (x ** 2 - 1) % n
        d = euclid(y - x, n)
        if d != 1 and d != n:
            print(d)
        if i == k:
            y = x
            k *= 2