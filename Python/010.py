from math import sqrt
from math import ceil

def is_prime(num):
    if (num%2 == 0):
        return 0
    for d in range(3, ceil(sqrt(num))+1, +2):
        if (num%d == 0):
            return 0
    return num

def sum_primes(upper):
    tot = 2;
    for n in range(3, upper, +2):
        tot += is_prime(n)
    print("Tot:", tot)

if __name__ == "__main__":
    sum_primes(int(2e6))
