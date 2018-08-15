import time

def is_my_pyta(a, b, c, num):
    return ((a < b < c) and (a*a + b*b == c*c) and (a + b + c == num))

def find_my_pyta(num):
    min_iter = 1
    max_iter = 1001
    for a in range(min_iter, max_iter):
        for b in range(min_iter, max_iter):
            for c in range(min_iter, max_iter):
                if is_my_pyta(a, b, c, num):
                    print(a, "*", b, "*", c, "=", a*b*c)
                    return
    print("Nope")
    return

if __name__ == "__main__":
    start = time.clock()
    find_my_pyta(1000)
    print("Elapsed:", time.clock() - start)
