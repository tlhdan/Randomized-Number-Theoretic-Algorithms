import secrets
from primality_testing import miller_rabin
from greatest_common_divisor import extended_euclid

def generate_prime(beta=1024):
    while True:
        num = secrets.randbits(beta)
        num |= (1 << (beta - 1))    # force top bit = 1
        num |= 1                    # force low bit = 1

        if miller_rabin(num):
            return num

def rsa():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = secrets.randbits(32)
    e |= 1
    d, x, y = extended_euclid(phi, e)
    while d != 1:
        e = secrets.randbits(32)
        e |= 1
        d, x, y = extended_euclid(phi, e)
    
    d = y % phi
    P = (e, n)
    S = (d, n)
    
    return P, S