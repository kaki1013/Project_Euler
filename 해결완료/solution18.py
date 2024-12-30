# 참고: (경로 최대합 문제) https://mingrammer.com/project-euler-maximum-path-sum/

number_list = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''.split()
triangle_list = []
for i in range(1, 16):
    triangle_list.append(number_list[int(i*(i-1)/2):int(i*(i+1)/2)])  # 끊기: [['75'], ['95', '64'], ...]

for i in range(0, 15):
    for j in range(0, i+1):
        triangle_list[i][j] = int(triangle_list[i][j])  # str에서 int로

for i in range(14, 0, -1):
    for j in range(0, i):
        if triangle_list[i][j] < triangle_list[i][j+1]:
            triangle_list[i-1][j] += int(triangle_list[i][j+1])
        else:
            triangle_list[i-1][j] += int(triangle_list[i][j])  # 아래부터 큰 값 선택

print(triangle_list[0][0])

# 연습용 코드
ex = [['1'], ['2', '3'], ['4', '5', '6']]
#   1
#  2 3
# 4 5 6
for i in range(0, 2):
    for j in range(0, i+1):
        ex[i][j] = int(ex[i][j])

for i in range(2, 0, -1):
    for j in range(0, i):
        if ex[i][j] < ex[i][j+1]:
            ex[i-1][j] += int(ex[i][j+1])
        else:
            ex[i-1][j] += int(ex[i][j])

print(ex[0][0])
