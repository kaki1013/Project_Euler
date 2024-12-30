def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def nth_10Permu(n):  # n번째 사전식 배열의 수 구하는 함수
    n_list = list(range(0, 10))  # [0,1,...,9]
    nth_num = []  # 구하는 수 list
    for i in range(9, -1, -1):
        if n != 0 and n % fact(i) != 0:  # n을 i!로 나눴을 때, 아직 0이 아닌 경우
            nth_num.append(n_list.pop(n // fact(i)))  # n을 i!로 나눈 몫(이하 '몫')의 인덱스를 추출해서 삽입
            n %= fact(i)  # n은 나머지로 치환
        elif n != 0 and n % fact(i) == 0:  # n을 i!로 나눴을 때, 0이 되는 차례인 경우
            nth_num.append(n_list.pop(n // fact(i) - 1))  # 마지막으로 나눌 때는, 하나 이전 수를 추출해서 대입
            n = 0  # 0으로 치환
        else:  # n이 0이 된 이후
            for j in range(len(n_list) - 1, -1, -1):
                nth_num.append(n_list[j])  # 남은 수들을 역순으로 대입
            break
    return nth_num  # 결과 반환


print(nth_10Permu(10 ** 6))