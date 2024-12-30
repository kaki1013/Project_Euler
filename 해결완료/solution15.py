# list.count(?) 함수는 리스트나 문자열에서 특정 element를 몇개 가지고 있는지 반환
# 방법0: 확통 풀듯이/ 40C20=137846528820

# 방법1: R(right), D(down) 각각 20개를 줄 세우는 방법의 수(RRDRD..)


# 방법2: 자리를 나타내는 1~40까지의 공을 R과 D라는 바구니에 각각 20개씩 담는 경우의 수


# 방법3: 합의 법칙과 점화식 사용 _ 큰 수에서는 오래 걸림
def count(a, b):
    if a == 1:
        return b + 1
    elif b == 1:
        return a + 1
    else:
        return count(a - 1, b) + count(a, b - 1)


print(count(2, 2))

# 방법4: 2^40가지 리스트(R과 D 총 40개 줄세움) 중 20개 20개 인 것의 개수 카운트// 메모리부족
situation = []
for i in range(2): situation.append([])  # 2**40+1로 바꿔야 함

# 방법5: [RR...R]에서 D를 20개 넣는 경우의 수 / x_1 + ... + x_21 = 20 (21H20)


# 방법6: 프로젝트 오일러에서..
l = []
for i in range(21):
    l.append([])  # [[]*21]
    for j in range(21):
        l[i].append(0)  # [[0*21]*21]

for i in range(21):
    l[20][i] = 1
    l[i][20] = 1  # [[0*20,1]*20,[1,1,...,1]]

for i in range(19, -1, -1):
    for j in range(19, -1, -1):
        l[i][j] = l[i + 1][j] + l[i][j + 1]  # 각 격자점에서 경로의 합 계산_ 표 생각
print(l[0][0])

# 방법7: 0과 1로 나타내서 2진법으로 생각
