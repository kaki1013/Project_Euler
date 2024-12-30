# 1: 15.230797052383423s  출처: https://soooprmx.com/archives/6392
def divisors(n):
    i = 2
    total = {1}
    while i <= n ** 0.5:
        if n % i == 0:
            total.add(i)
            total.add(n / i)
        i += 1
    return sum(total)


abun = set()
for i in range(1, 28123):
    if i < divisors(i):
        abun.add(i)

numbers = set(range(1, 28123))
for i in abun:
    for j in abun:
        if (i + j) in numbers:
            numbers.remove(i + j)
print(sum(numbers))

# 2: ?분 ?시간
abundant_number = []
answer = []
n = 28123

for x in range(2, n + 1):
    sum_div = 1
    for d in range(x // 2, 1, -1):
        if x % d == 0:
            sum_div += d
            if sum_div > x:
                abundant_number.append(x)
                break

for i in range(1, n + 1):
    for an in abundant_number:
        if (i - an) in abundant_number:
            break
    else:
        answer.append(i)

s = 0
for y in answer:
    s += y
print(s)

# 3: 7.326404094696045s // 답 다름
def abun(N):
    Q = dict.fromkeys(range(1, N + 1), 0)
    for q in Q:
        for k in [q * n for n in range(1, N // q + 1)]:
            if q != k:
                Q[k] += q
    return [q for q in Q if Q[q] > q]


N = 20161
A = abun(N)
possible = set()
for a in A:
    for b in A:
        if a + b < N:
            possible.add(a + b)
        else:
            break

print(sum([p for p in range(N) if p not in possible]))

# 4: 1.338066577911377s
def PE023(limit=28123):
    somDiv = [1] * (limit + 1)  # jusk 28123 inclus
    for i in range(2, int(limit ** .5) + 1):
        somDiv[i * i] += i
        for k in range(i + 1, limit // i + 1):
            somDiv[k * i] += k + i
    abondant, res = set(), 0
    ajout = abondant.add
    for n in range(1, limit + 1):
        if somDiv[n] > n: ajout(n)
        if not any((n - a in abondant) for a in abondant): res += n
    return res
print(PE023(28123))

# 5: 1.3434319496154785
def d(n):
    m, s = n ** 0.5, 1
    if m == int(m): s -= int(m)
    m = int(m // 1) + 1
    for i in range(2, m):
        if n % i == 0: s += i + (n / i)
    return s

a, s = set(), 0
for i in range(1, 20612):
    if d(i) > i: a.add(i)
    if not any((i - j) in a for j in a): s += i
print(s)

# 6 : 14.517309427261353s
def div(n):
    s = {1}
    for r in range(2, int(n**0.5)+1):
        if n % r == 0:
            s.add(r)
            s.add(n//r)
    return sum(s)

ab = set(i for i in range(1,30000) if div(i) > i)
ss = set(x+y for x in ab for y in ab)
zs = set(range(1,28124))
print(sum(zs - ss))