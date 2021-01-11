# 1
def a_n(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return a_n(n - 1) + a_n(n - 2)


sum = 0
i = 2

# a_2+a_5+...

while a_n(i) < 4000000:
    sum += a_n(i)
    i += 3

print(sum)


# 2
# 1,1롤 시작하는 피보나치: O, O, E, O, O, E, O, O, E,.. 로 3번째마다 짝수
# x, y, x + y, x + 2y, 2x + 3y, 3x + 5y, ...

def calc():
    x = y = 1
    sum = 0
    while (y< 4000000):
        sum += (x + y)
        x, y = x + 2 * y, 2 * x + 3 * y
    return sum

print(calc())