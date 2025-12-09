import random
from modular_exponentiation import modular_exponentiation

def witness(a, n):
    u = n - 1
    t = 0
    while u % 2 == 0:
        u //= 2
        t += 1
    
    previous_x = modular_exponentiation(a, u, n)
    for _ in range(t):
        x = previous_x ** 2 % n
        if x == 1 and previous_x != 1 and previous_x != n - 1:
            return True
        previous_x = x
    
    if x != 1:
        return True
    
    return False

def miller_rabin(n, s=50):
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for _ in range(s):
        a = random.randint(1, n - 1)
        if witness(a, n):
            return False
        
    return True