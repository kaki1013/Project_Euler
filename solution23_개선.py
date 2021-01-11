# 5.49873685836792s
abun_list = []  # 28123 미만의 모든 과잉수 목록 생성
for n in range(1, 28124):
    div_list = [1]
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            div_list.append(d)
            div_list.append(n // d)
            div_list = list(set(div_list))
    if sum(div_list) > n:
        abun_list.append(n)
abun_set = set(abun_list)  # 이후 소속검사를 빠르게 하기 위해서//안하면 9~10분 걸림

# 1부터 28123까지의 합에서 과잉수 두개의 합으로 표현가능한 수를 빼기
cannot = 28123*28124//2
for n in range(1, 28124):
    for i in range(0, len(abun_list)):
        if (abun_list[i] < n//2 + 1) and (n - abun_list[i] in abun_set):  # n//2 이하의 과잉수만 보기
            cannot -= n  # 괴잉수 2개의 합으로 표현되면 빼기
            break  # 다음 n 탐색
        if abun_list[i] >= n//2 + 1:
            break  # 다음 n 탐색

print(cannot)
