import secrets
from src.primality_testing import is_prime
from src.greatest_common_divisor import euclid as gcd, extended_euclid
from src.modular_exponentiation import modular_exponentiation
from src.integer_factorization import factorize

def generate_prime(beta):
    while True:
        num = secrets.randbits(beta)
        num |= (1 << (beta - 1))    # force top bit = 1
        num |= 1                    # force low bit = 1

        if is_prime(num):
            return num

def rsa_key_generation(beta=1024, pub_e=True):
    if pub_e:
        e = 65537

        p = generate_prime(beta // 2)
        while p % e == 1:
            p = generate_prime(beta // 2)
        
        q = generate_prime(beta - beta // 2)
        while q % e == 1 or q == p:
            q = generate_prime(beta - beta // 2)

    else:
        p = generate_prime(beta // 2)
        q = generate_prime(beta - beta // 2)
        while q == p:
            q = generate_prime(beta - beta // 2)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    if not pub_e:
        e = secrets.randbits(32)
        e |= 1

        while gcd(e, phi_n) != 1:
            e = secrets.randbits(32)
            e |= 1

    g, x, y = extended_euclid(phi_n, e)
    while g != 1:
        e = secrets.randbits(32)
        e |= 1
        g, x, y = extended_euclid(phi_n, e)
    
    d = y % phi_n
    P = (e, n)
    S = (d, n)
    
    return P, S

def encrypt(m, e, n):
    return modular_exponentiation(m, e, n)

def decrypt(c, d, n):
    return modular_exponentiation(c, d, n)    

def attack(c, e, n):
    fact_n = factorize(n)

    if len(fact_n) != 2:
        raise Exception("Invalid modulo for RSA")
    
    factors = list(fact_n.keys())
    p, q = factors[0], factors[1]
    phi_n = (p - 1) * (q - 1)

    g, x, y = extended_euclid(phi_n, e)

    if g != 1:
        raise Exception("Invalid public exponent")
    
    d = y % phi_n
    
    c_p = c % p
    c_q = c % q

    d_p = d % (p - 1)
    d_q = d % (q - 1)

    x_p = modular_exponentiation(c_p, d_p, p)
    x_q = modular_exponentiation(c_q, d_q, q)

    _, c_p, _ = extended_euclid(q, p)
    _, c_q, _ = extended_euclid(p, q)

    m = (q * c_p * x_p + p * c_q * x_q) % (p * q)

    return m