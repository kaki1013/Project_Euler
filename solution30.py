"""
As 1 = 1^4 is not a sum it is not included.
9^5=59049
n-digit : 10^(n-1) ~ 10^n-1
the range of the sum of fifth powers of n-digits: 1 ~ 59049 * n
10^(n-1) <= 59049n  =>  n < 6

"""
def fifth_sum(x):
    temp = list(str(x))
    return sum([int(i)**5 for i in temp])

ans = -1    # 1은 포함 X
for n in range(10**6):
    if fifth_sum(n) == n:
        ans += n
print(ans)
