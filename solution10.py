primes = [2]

for i in range(3, 2000000, 2):
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            break
    else:
        primes.append(i)

print(sum(primes))

# others
n = 2000000
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
    for j in range(2 * i, n + 1, i):
        a[j] = False

print(len(primes), primes[-1], sum(primes))

# 에라토스테네스 체와 집합 자료형_더 빠름
max_num = 2000000

prime_numbers = set(range(2,max_num+1))

for i in range(2,int(max_num ** 0.5)+1):
    if i * 2 <= max_num:
        prime_numbers -= set(range(i * 2,max_num+1,i))

result = 0
for i in list(prime_numbers): result += i

print(result)