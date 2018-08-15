import math

def is_prime(num):
    if (num%2 == 0):
        return False
    for d in range(3, math.ceil(math.sqrt(num))):
        if (num%d == 0):
            return False
    return True

def factorize(num):
    for d in range(3, math.ceil(math.sqrt(num))):
        if (num%d == 0):
            if (is_prime(num/d)):
                print("Bigger:", num/d)
            num /= d
        else:
            d += 2

if __name__ == "__main__":
    factorize(600851475143)
