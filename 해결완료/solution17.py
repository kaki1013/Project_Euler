# 1-3, 2-3, 3-5, 4-4, 5-4, 6-3, 7-5, 8-5, 9-4, 10-3
# 11-6, 12-6, 13-8, 14-8, 15-7, 16-7, 17-9, 18-8, 19-8
# 20-6, 30-6, 40-5, 50-5, 60-5, 70-7, 80-6, 90-6, X00-7
# dict 사용도 가능

def letter_count_1(num):  # 한 자리 letter 반환/ input: 1~9
    if num == 0:
        return 0
    elif num in [1, 2, 6]:
        return 3
    elif num in [3, 7, 8]:
        return 5
    else:
        return 4


def letter_count_2(num):  # 두 자리 letter 반환/ input: 10~99
    if num in range(10, 20):
        if num == 10:
            return 3
        elif num == 17:
            return 9
        elif num in [11, 12]:
            return 6
        elif num in [15, 16]:
            return 7
        else:
            return 8
    else:
        if num//10 == 7:
            return 7 + letter_count_1(num % 10)
        elif num//10 in [4, 5, 6]:
            return 5 + letter_count_1(num % 10)
        else:
            return 6 + letter_count_1(num % 10)


num_list = []  # letter count list
for i in range(1, 1000):
    if len(str(i)) == 1:
        num_list.append(letter_count_1(i))
    elif len(str(i)) == 2:
        num_list.append(letter_count_2(i))
    else:
        if i % 100 == 0:
            num_list.append(letter_count_1(i // 100) + 7)
        elif len(str(i % 100)) == 1:
            num_list.append(letter_count_1(i // 100) + 7 + 3 + letter_count_1(i % 100))  # hundred, and
        else:
            num_list.append(letter_count_1(i // 100) + 7 + 3 + letter_count_2(i % 100))  # hundred, and
num_list.append(11)  # 1000(one thousand): 11
print(sum(num_list))

# 오류 확인용_list 20개씩 끊음
for i in range(1, 51):
    print(num_list[20*(i-1):20*i])
