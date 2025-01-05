"""
when digit = n,
range of possible numbers : 10^(n-1) ~ 10^n-1
range of possible sums : n ~ 362880n

By check 1, we can get proper boundary (under 10^8) to solve this problem

# [check 1]
for i in range(1, 1000):
    if 10**(i-1) > factorial[9] * i:
        print(i)
        break
# output : 8
"""
factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def is_curious(n):
    n_ = n
    check = 0
    while n:
        check += factorial[n % 10]
        n //= 10
    return n_ == check


ans = 0
for i in range(3, 10**8):
    if is_curious(i):
        ans += i
        print(i)

print(ans)
