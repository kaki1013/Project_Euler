def day_num(dd, mm, yyyy):  # 날짜를 요일로 대응하는 함수
    num = 0
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    years = []
    for i in range(1900, 2001):
        if i % 4 != 0:  # 윤년 아님
            years.append(365)
        elif i % 100 != 0:  # 윤년
            years.append(366)
        elif i % 400 != 0:  # 윤년 아님
            years.append(365)
        else:  # 윤
            years.append(366)
    for i in range(0, yyyy - 1900):  # yyyy-1 년까지
        num += years[i]
    if years[yyyy - 1900] == 366 and ((mm, dd) == (2, 29) or mm > 2):  # yyyy 년이 윤년? & 2월 이전 이후 구분해서
        num += 1
    for i in range(1, mm):  # mm-1 월까지
        num += months[i]
    num += dd - 1  # dd일 계산
    num += 1  # 일요일이 7의 배수가 되도록
    return num % 7  # Mon-1, ..., Sun-7(0)


count = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if day_num(1, j, i) % 7 == 0:
            count += 1
print(count)

#  https://opentutorials.org/module/2980/17775
daylist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0
count = 0

for y in range(1900, 2001):
    for m in range(12):
        day = daylist[m]
        if y % 4 == 0 and m == 1:
            day += 1
        for d in range(day):
            if y > 1900 and d == 0 and total % 7 == 6:
                count += 1
            total += 1

print(total, count)