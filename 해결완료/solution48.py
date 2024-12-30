ans = 0

for i in range(1, 1001):
    ans = (ans + i**i) % 10 ** 10

print(ans)