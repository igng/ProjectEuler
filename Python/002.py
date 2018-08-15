def short_version(upper):
    prev_fib = 1;
    curr_fib = 1;
    next_fib = 0;
    tot = 0;
    while (next_fib < upper):
        tot += next_fib if (not (next_fib%2)) else 0
        next_fib = curr_fib + prev_fib;
        prev_fib = curr_fib;
        curr_fib = next_fib;
        print("next:", next_fib)
    print("\ntot:", tot);


if __name__ == "__main__":
    short_version(4000000)
