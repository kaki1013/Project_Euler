def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 연습: [0,1,2,3,4] when n=100 -> ans: 40231
# 4!*4 -> 4(=l[4]), n= 100-4!*4(=4)
# 3!*0 -> 0(=l[0]), n= 4-3!*0(=4)
# 2!*2 -> 2(=l[1]), n= 4-2!*2(=0)
# n=0 이므로 남은 수들(1,3) 역순으로 나열: 40231
# 40 123 / 40 131 / 40 213 / 40 231
# 단 [4][0] 이후 0이라면? 남은 리스트의 index[0]을 꺼내면 됨
# 99일 때는 40213


def nth_5Permu(n):
    n_list = [0, 1, 2, 3, 4]
    nth_num = []
    for i in [4, 3, 2, 1, 0]:
        if n != 0 and n % fact(i) != 0:
            nth_num.append(n_list.pop(n // fact(i)))
            n %= fact(i)
        elif n != 0 and n % fact(i) == 0:
            nth_num.append(n_list.pop(n // fact(i) - 1))
            n %= fact(i)
        else:
            for j in range(len(n_list) - 1, -1, -1):
                nth_num.append(n_list[j])
            break
    return nth_num


for i in range(1, 121):
    print(nth_5Permu(i))
