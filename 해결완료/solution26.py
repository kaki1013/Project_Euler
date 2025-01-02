# https://kaki1013.tistory.com/entry/%EC%88%9C%ED%99%98%EC%86%8C%EC%88%98
def get_coprime(n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    return n


def get_period(n):
    p = 1
    while int('9' * p) % n != 0:
        p += 1
    return p


arr = [0] * 1000
for i in range(1, 1000):
    n = get_coprime(i)
    if n == i:
        arr[i] = get_period(i)
    else:
        arr[i] = arr[n]

m = max(arr)
for i in range(1, 1000):
    if arr[i] == m:
        print(i)
