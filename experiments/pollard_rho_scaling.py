import random
import matplotlib.pyplot as plt
from src.greatest_common_divisor import euclid as gcd
from src.rsa import generate_prime

def pollard_rho(n, c_random=True, c=-1):
    iterations = 0

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
                return iterations
            
            if i == k:
                y = x
                k *= 2

def balanced_test(B_lst=[16, 20, 24, 28, 32], num_semiprimes=50, num_trials=20):
    normalized_iters_lst = []

    for beta in B_lst:
        semiprimes = []

        for _ in range(num_semiprimes):
            p = generate_prime(beta // 2)
            q = generate_prime(beta - beta // 2)
            semiprimes.append(p * q)
        
        total_iters = 0
        for semiprime in semiprimes:
            for _ in range(num_trials):
                total_iters += pollard_rho(semiprime)
        
        avg_iters = total_iters / (num_semiprimes * num_trials)
        normalized_iters = avg_iters / min(p, q) ** 0.5
        normalized_iters_lst.append(normalized_iters)

        print(f'B = {beta}:\tAverage iterations: {avg_iters}\tNormalized iterations: {normalized_iters}')
    
    plt.figure()
    plt.plot(B_lst, normalized_iters_lst, marker='o')
    plt.xlabel("Bit-length")
    plt.ylabel("Normalized iterations")
    plt.title("Normalized Pollard's rho runtime on balanced semiprimes")
    plt.ylim(0, 2)

    for x, y in zip(B_lst, normalized_iters_lst):
        plt.annotate(
            f"{y:.3g}",
            (x, y),
            textcoords="offset points",
            xytext=(0, 8),
            ha='center'
        )

    plt.show()

def unbalanced_test(B_lst=[16, 32, 48, 64, 80, 96], num_semiprimes=50, num_trials=20):
    avg_iters_lst = []

    for beta in B_lst[1:]:
        semiprimes = []

        for _ in range(num_semiprimes):
            p = generate_prime(B_lst[0])
            q = generate_prime(beta)
            semiprimes.append(p * q)
        
        total_iters = 0
        for semiprime in semiprimes:
            for _ in range(num_trials):
                total_iters += pollard_rho(semiprime)
        
        avg_iters = total_iters / (num_semiprimes * num_trials)
        avg_iters_lst.append(avg_iters)

        print(f'B = {B_lst[0]} x {beta}:\tAverage iterations: {avg_iters}')
    
    plt.figure()
    plt.plot(B_lst[1:], avg_iters_lst, marker='o')
    plt.xlabel("q's bit-length")
    plt.ylabel("Average iterations")
    plt.title("Pollard's rho runtime on unbalanced semiprimes")
    plt.ylim(0, 500)

    for x, y in zip(B_lst[1:], avg_iters_lst):
        plt.annotate(
            f"{y:.3g}",
            (x, y),
            textcoords="offset points",
            xytext=(0, 8),
            ha='center'
        )

    plt.show()

balanced_test()
unbalanced_test()