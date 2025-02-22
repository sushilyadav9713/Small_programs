import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(4, int(n / 2)):
        if n % i == 0:
            return False
    return True


n = 6
