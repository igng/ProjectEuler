import time

def reverse(n, num):
    for d in range(num, 10, -1):
        if (n%d):
            return False
    return True

def find_smallest_divis(num):
    start = time.clock()
    n = 20
    while True:
        if (reverse(n, num)):
            print("Smallest:", n)
            print("\nElapsed:", time.clock() - start)
            return
        n += 2

if __name__ == "__main__":
    find_smallest_divis(20)
