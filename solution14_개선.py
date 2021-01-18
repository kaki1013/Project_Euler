# 83.87875270843506s
max_step = 0
max_index = 0
for i in range(1, 10 ** 6 + 1):
    step = 0
    num = i
    while not num == 1:
        step += 1
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
    if step > max_step:
        max_step = step
        max_index = i
print(max_index)


# others1: 3.113677740097046s
def collatz(n): return n // 2 if n % 2 == 0 else 3 * n + 1


def distance(n, cache={1: 1}):
    if n not in cache: cache[n] = distance(collatz(n)) + 1
    return cache[n]


print(max(range(1, 1000000), key=distance))


# others2: 3.403927803039551s
def longest_collatz_sequence(t):
    cache = {1: 1}

    def collatz_(n):
        if n not in cache:
            cache[n] = collatz_(3 * n + 1 if n % 2 else n / 2) + 1
        return cache[n]  # Length of Collatz Chain

    return max(range(1, t), key=collatz_)  # Greatest Chain


print(longest_collatz_sequence(1000000))
