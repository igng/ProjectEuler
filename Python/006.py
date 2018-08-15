def difference(n):
    Ss = 0
    sS = 0
    for i in range(1, n+1):
        Ss += (i*i)
        sS += i
    print("Diff:", sS*sS - Ss)

if __name__ == "__main__":
    difference(100)
