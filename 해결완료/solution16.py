# 방법 1: 계산하고 리스트 만들어서 합
two_power = list(str(2**1000))
digit_sum = 0
for i in range(1, len(two_power) + 1):
    digit_sum += int(two_power[i-1])
print(digit_sum)

# 방법 1 개선: for 문 범위는 문자열, 리스트, 튜플 가능
digit_sum_re = 0
for n in str(2**1000):
    digit_sum_re += int(n)
print(digit_sum_re)

# 방법 2: 자리수로 리스트 만들기/ 안함
digit_list = []
for i in range(1, 1000+1):
        break