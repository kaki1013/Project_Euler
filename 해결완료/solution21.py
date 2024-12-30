def d(n):
    div_list = [1]  # n은 미포함
    for i in range(2, int(n**0.5)+1):  # n>2
        if n % i == 0:
            div_list.append(i)
            div_list.append(n//i)
    div_list = list(set(div_list))  # 제곱수일 때 중복 원소 제거
    return sum(div_list)


amicable_list = []
for i in range(1, 10001):
    if d(d(i)) == i and d(i) != i:  # d(i)=j, d(j)=i 이고 i != j
        amicable_list.append(i)
print(amicable_list)
print(sum(amicable_list))
