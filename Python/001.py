def short_version(upper):
    tot = 0;
    for i in range(1, upper):
        tot += i if (not (i%3) or not (i%5)) else 0
    print("\ntot:", tot)

if __name__ == "__main__":
    short_version(1000)
