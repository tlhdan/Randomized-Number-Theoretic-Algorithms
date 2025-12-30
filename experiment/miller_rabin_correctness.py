import secrets
import matplotlib.pyplot as plt
from src.primality_testing import miller_rabin

def prime_test(s_lst=[1, 5, 25, 50]):
    print('Error rate when input is prime:')

    for s in s_lst:
        cnt = 0

        with open('experiment/lists/small_primes.txt', 'r') as f:
            primes = [line.rstrip('\n') for line in f.readlines()]

        for prime in primes:
            prime = int(prime)
            if not miller_rabin(prime, s):  # returns composite when prime
                cnt += 1
        
        p = cnt / 1228 * 100
        print(f'\ts = {s}: {p}%')

def carmichael_test(s_lst=[1, 2, 4, 8, 16], num_trials=50):
    error_rates = []
    print('Error rate when input is a Carmichael number:')

    for s in s_lst:
        cnt = 0

        with open('experiment/lists/carmichael_numbers.txt', 'r') as f:
            carmichael_numbers = [line.rstrip('\n') for line in f.readlines()]

        for carmichael_number in carmichael_numbers:
            for _ in range(num_trials):
                carmichael_number = int(carmichael_number)
                if miller_rabin(carmichael_number, s):  # returns prime when composite
                    cnt += 1
        
        p = cnt / (600 * num_trials) * 100
        error_rates.append(p)
        print(f'\ts = {s}: {p}%')
    
    plt.figure()
    plt.plot(s_lst, error_rates, marker='o')
    plt.xlabel("Number of rounds (s)")
    plt.ylabel("Error rate (%)")
    plt.title("Miller–Rabin's error rate on Carmichael numbers")
    plt.ylim(0, 4.2)

    for x, y in zip(s_lst, error_rates):
        plt.annotate(
            f"{y:.3g}%",
            (x, y),
            textcoords="offset points",
            xytext=(0, 8),
            ha='center'
        )

    plt.show()

def random_odd_composite_test(s_lst=[1, 2, 4, 8, 16], B_lst=[16, 20, 24, 28, 30, 32, 40], num_trials=1000):
    print('Error rate when input is a random odd composite:')

    odd_composites = []
    
    for beta in B_lst:
        cnt = 0
        while cnt != num_trials:
            num = secrets.randbits(beta)
            num |= (1 << (beta - 1))
            num |= 1

            if not miller_rabin(num, 50):   # odd composite
                odd_composites.append(num)
                cnt += 1
                
    for s in s_lst:
        cnt = 0

        for odd_composite in odd_composites:
            if miller_rabin(odd_composite, s):  # returns prime when composite
                cnt += 1
        
        p = cnt / (len(B_lst) * num_trials) * 100
        print(f'\ts = {s}: {p}%')

carmichael_test()
random_odd_composite_test()