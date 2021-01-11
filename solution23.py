# 619.4685509204865s

def id_abundant(n):  # 과잉수 판별기
    div_list = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            div_list.append(i)
            div_list.append(n // i)
            div_list = list(set(div_list))
    if sum(div_list) > n:
        return True
    else:
        return False


abun_list = []  # 28123 미만의 모든 과잉수 목록 생성
for i in range(1, 28124):
    if id_abundant(i):
        abun_list.append(i)

# 28123 이하의 정수들 중 과잉수 두개의 합으로 표현할 수 없는 수들의 리스트 생성
cannot = list(range(1, 28124))
for n in range(1, 28124):
    for i in range(0, len(abun_list)):
        if (abun_list[i] < n) and (n - abun_list[i] in abun_list):
            cannot.remove(n)
            break
        if abun_list[i] >= n:
            break

print(sum(cannot))
