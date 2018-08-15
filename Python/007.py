from math import sqrt
from math import ceil

def is_prime(n):
    if (n%2 == 0):
        return False
    for d in range(3, ceil(sqrt(n) + 1)):
        if (n%d == 0):
            return False
    return True

def count_primes(upper):
    i = 2
    n = 3
    while (i < upper):
        n += 2
        if (is_prime(n)):
            i += 1
            #print(i, "|", n)
    print("\n", n)


if __name__ == "__main__":
    count_primes(10001)
