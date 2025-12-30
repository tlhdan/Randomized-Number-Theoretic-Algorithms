import random
from src.greatest_common_divisor import euclid as gcd
from src.rsa import generate_prime

def pollard_rho(n, c_random=True, c=-1):
    iterations = 0
    restarts = 0

    while True:
        i = 1
        x = random.randint(0, n - 1)
        y = x
        k = 2
        if c_random:
            c = random.randint(1, n - 1)

        for _ in range(int(5 * n ** 0.25)):
            iterations += 1
            i += 1
            x = (x ** 2 + c) % n
            d = gcd(y - x, n)

            if d != 1 and d != n:
                return iterations, restarts
            
            if i == k:
                y = x
                k *= 2
        
        restarts += 1

def test_c(c, semiprimes_lst, num_semiprimes, num_trials, c_random=False):
    total_iters = 0
    total_avg_iters_per_attempt = 0
    total_restarts = 0

    for semiprime in semiprimes_lst:
        for _ in range(num_trials):
            iterations, restarts = pollard_rho(semiprime, c_random, c)
            total_iters += iterations
            total_restarts += restarts
            total_avg_iters_per_attempt += iterations / (restarts + 1)
        
    avg_total_iters = total_iters / (num_semiprimes * num_trials)
    avg_iters_per_attempt = total_avg_iters_per_attempt / (num_semiprimes * num_trials)
    avg_restarts = total_restarts / (num_semiprimes * num_trials)

    if not c_random:
        print(f'c = {c}:\t\tMean total iterations: {avg_total_iters:.2f}\tAverage iterations per attempt: {avg_iters_per_attempt:.2f}\tAverage restarts: {avg_restarts}')
    else:
        print(f'Random c:\tMean total iterations: {avg_total_iters:.2f}\tAverage iterations per attempt: {avg_iters_per_attempt:.2f}\tAverage restarts: {avg_restarts}')

def test(c_lst=[-1, 1, 2, 3], test_random_c=True, num_semiprimes=200, num_trials=20):
    semiprimes = []
    for _ in range(num_semiprimes):
        p = generate_prime(16)
        q = generate_prime(16)
        semiprimes.append(p * q)
    
    for c in c_lst:
        test_c(c, semiprimes, num_semiprimes, num_trials)

    if test_random_c:
        test_c(0, semiprimes, num_semiprimes, num_trials, True)

test()