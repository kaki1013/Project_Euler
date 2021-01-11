# 최대 시행 횟수와 그 수를 기록 후 더 오래 걸리면 교체?
def collatz(num):
    if num % 2 == 0:
        num /= 2
    else:
        num = 3 * num + 1
    return int(num)


step_list = []

for i in range(1, 10 ** 6 + 1):
    step = 0
    num = i
    while not num == 1:
        step += 1
        num = collatz(num)
    step_list.append(step)

longest = step_list.index(max(step_list))
# index 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려주는 위치반환

print(longest + 1)
