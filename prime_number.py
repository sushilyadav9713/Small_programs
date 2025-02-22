# Import the necessary library for prime checking
import math


# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


# Function to find Mersenne primes
def find_mersenne_primes(limit):
    mersenne_primes = []
    for p in range(2, limit):
        if is_prime(p):
            mersenne = 2**p - 1
            if is_prime(mersenne):
                mersenne_primes.append(mersenne)
    return mersenne_primes


# Input limit for searching Mersenne primes
limit = 10  # You can adjust this limit

# Find and print Mersenne primes
mersenne_primes = find_mersenne_primes(limit)
print(f"Mersenne primes up to 2^{limit} - 1: {mersenne_primes}")
print(f"{2**62 - 1}")
