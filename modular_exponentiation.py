def modular_exponentiation(a, b, n):
    c = 0
    d = 1
    b = bin(b)[:2]
    for i in b:
        c *= 2
        d = d ** 2 % n
        if i == 1:
            c += 1
            d = d * a % n
    return d