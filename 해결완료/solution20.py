def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n


num = factorial(100)
digit_list = list(str(factorial(100)))
digit_sum = 0
for i in digit_list:
    digit_sum += int(i)
print(digit_sum)
