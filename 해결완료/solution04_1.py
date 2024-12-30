# 3자리 수 2개의 곱 리스트 작성(내림차순)/ 숫자의 자리수를 리스트로 만든 뒤 [::-1]과 일치시 회문수로 판단

# 3자리 수 2개의 곱 목록_227521개(중복X)
numbers = []

for i in range(100, 1000):
    for j in range(100, 1000):
        numbers.append(i * j)

number_list=list(set(numbers))
number_list.sort(reverse=True)      # 내림차순

# 자리수 리스트 만들기
# 그냥 str() 써도 됨..
def 자리수_리스트(x):
    digit_list=[]
    while x>9:
        digit_list.append(x%10)
        x=x//10
    else:
        digit_list.append(x)
    return digit_list[::-1]

# 회문수인지만 체크: 각 자리수를 차례대로 리스트로 만들고, -1 슬라이싱과 일치시 회문수_True
def 회문수(x):
    if 자리수_리스트(x) == 자리수_리스트(x)[::-1]:
        return True

for i in number_list:
    if 회문수(i) == True:
        print(i)
        break


# 함수 없이 '정리'한 코드
numbers = []                        # 입력할 리스트 생성

for i in range(100, 1000):
    for j in range(100, 1000):
        numbers.append(i * j)       # 3자리수 2개를 곱한 수들을 원소로 추가

number_list=list(set(numbers))      # 중복제거 (101*345=345*101 같은 수들은 중복)
number_list.sort(reverse=True)      # 내림차순

for i in number_list:
    digit_list = []
    while i > 9:
        digit_list.append(i % 10)   # 일의 자리 수부터 자릿수 리스트에 추가
        i = i // 10                 # 원래 수 자리에 원래 수를 10으로 나눈 몫을 대입
    else:
        digit_list.append(i)        # 마지막으로 가장 큰 자릿수 리스트에 추가
    if digit_list == digit_list[::-1]:  # 거꾸로 된 자릿수 리스트 = 제대로 된 자릿수 이면
        print(digit_list)           # 그 수를 출력
        break                       # 이후는 실행할 필요 X

# 정리_최종 0.45s
numbers = []                        # 입력할 리스트 생성

for i in range(100, 1000):
    for j in range(100, 1000):
        numbers.append(i * j)       # 3자리수 2개를 곱한 수들을 원소로 추가

number_list=list(set(numbers))      # 중복제거 (101*345=345*101 같은 수들은 중복)
number_list.sort(reverse=True)      # 내림차순

for i in number_list:
    if str(i) == str(i)[::-1]:      # 거꾸로 된 자릿수 리스트 = 제대로 된 자릿수 이면
        print(i)                    # 그 수를 출력
        break                       # 이후는 실행할 필요 X