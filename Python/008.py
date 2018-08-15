def get_number():
    with open("008.txt", 'r') as f:
        lines = f.read().splitlines()
        return "".join(lines)

def check_sequence(length):
    n = get_number()
    l = len(n)
    bigger = 0
    for i in range(0, l-length):
        seq = n[i:i+length]
        prod = 1;
        for k in seq:
            prod *= int(k)
        if (prod > bigger):
            bigger = prod
    print(bigger)

if __name__ == "__main__":
    check_sequence(13)
