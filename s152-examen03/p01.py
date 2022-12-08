def count_digits(n):
    ans = 0
    while(n > 0):
        ans += 1
        n //= 10
    return ans

def extract_list(values, k):
    ans = []
    digits = count_digits(k)    
    for x in values:
        if count_digits(x) == digits:
            ans.append(x)
    return ans

if __name__ == "__main__":
    A = [120, 3, 44, 260]
    k = 900
    print(extract_list(A, k))