def is_prime(digit):
    return digit in [2, 3, 5, 7]
    #return digit == 2 or digit == 3 or digit == 5 or digit == 7

def extract_number(n):
    factor = 1
    ans = 0
    while n > 0:
        digit = n % 10
        if is_prime(digit):
            ans += factor * digit
            factor *= 10
        n //= 10
    return ans


if __name__ == "__main__":
    print(is_prime(7))
    print(is_prime(2))
    print(is_prime(4))
    print(extract_number(67123))