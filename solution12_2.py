# 13.149838s
def factors(n):
    factor_list = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factor_list.append(i)
            factor_list.append(n // i)
    return factor_list


i = 1

while len(factors(i * (i + 1) / 2)) < 500:
    i += 1
print(i * (i + 1) / 2)
