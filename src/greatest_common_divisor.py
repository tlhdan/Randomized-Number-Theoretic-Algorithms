def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d_, x_, y_ = extended_euclid(b, a % b)
        d, x, y = d_, y_, x_ - a // b * y_
        return d, x, y