def is_palindrome(num):
    return (str(num) == str(num)[::-1])

def check_bigger_palindrome():
    bigger = 0;
    for left in range(100, 1000):
        for right in range(100, 1000):
            prod = left*right
            if ((is_palindrome(prod)) and (prod > bigger)):
                bigger = prod
    print("Bigger:", bigger)

if __name__ == "__main__":
    check_bigger_palindrome()
