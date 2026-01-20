# Random Number-Theoretic Algorithms

## Overview

This repository contains Python implementations of several fundamental number-theoretic algorithms commonly used in cryptography. The project focuses on the theoretical foundations, correctness, and empirical behavior of probabilistic primality testing and integer factorization algorithms, supported by experimental evaluation.

The implemented algorithms include the Miller–Rabin primality test, Pollard’s rho factorization algorithm, and a basic RSA cryptosystem built on top of these components.

---

## Implemented Algorithms

- Euclid's algorithm
- Extended Euclid algorithm
- Modular exponentiation
- Miller–Rabin algorithm
- Pollard’s rho algorithm
- RSA Cryptosystem
  - Key generation
  - Encryption and decryption
  - Basic factorization-based attack

---

## Project Structure
```bash
.
├── experiments/
│ ├── lists/
│ │ ├── carmichael_numbers.txt
│ │ └── small_primes.txt
│ ├── miller_rabin_correctness.py
│ ├── pollard_rho_scaling.py
│ └── pollard_rho_success_rate.py
├── src/
│ ├── greatest_common_divisor.py
│ ├── integer_factorization.py
│ ├── modular_exponentiation.py
│ ├── primality_testing.py
│ └── rsa.py
└── README.md
```

The `experiments/` directory contains scripts and datasets used to evaluate the behavior of the algorithms.

---

## Requirements

- **Python**: 3.11.5

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tlhdan/Randomized-Number-Theoretic-Algorithms
   ```

2. Navigate into the project directory:
   ```bash
   cd Random-Number-Theoretic-Algorithms
   ```

---

## How to run

All implemented algorithms can be used by importing the functions into an interactive Python session.
   ```bash
   python
   from src.<module> import <function>
   ```

Example:
   ```bash
   python
   >>> from src.greatest_common_divisor import euclid
   >>> euclid(21, 7)
   7
   ```

---

## Available Functions

The following functions are provided by the modules in the `src/` directory.

#### `greatest_common_divisor.py`

- `euclid(a, b)`  
  Computes the greatest common divisor of integers `a` and `b` using the Euclid's algorithm.

- `extended_euclid(a, b)`  
  Computes the greatest common divisor of `a` and `b` and returns the coefficients of Bézout’s identity.

#### `modular_exponentiation.py`

- `modular_exponentiation(a, b, n)`  
  Computes `a^b mod n` efficiently using repeated squaring.

#### `primality_testing.py`

- `is_prime(n)`  
  Determines whether the integer `n` is prime using the Miller–Rabin probabilistic primality test.

#### `integer_factorization.py`

- `factorize(n)`  
  Factor the integer `n` into its prime factors using Pollard’s rho algorithm.

#### `rsa.py`

- `key_generation(beta=1024, pub_e=True)`  
  Generates an RSA key pair. The parameter `beta` specifies the bit-length of the modulus. If `pub_e` is set to `True`, the public exponent is fixed to 65537; otherwise, it is chosen at random.

- `encrypt(m, e, n)`  
  Encrypts the plaintext integer `m` using the public key \(e, n\).

- `decrypt(c, d, n)`  
  Decrypts the ciphertext integer `c` using the private key \(d, n\).

- `attack(c, e, n)`  
  Demonstrates a basic factorization-based attack on RSA by attempting to recover the private key from the public parameters.

---  

## Notes

This project is intended for educational and experimental purposes. The implementations are not optimized for large-scale cryptographic deployment, and no guarantees are made regarding security against real-world attacks.