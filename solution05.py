# 1~20의 최소공배수: 232792560

# 1 1부터 20까지의 수로 모두 나눠지는 최소의 수를 1부터 차례로 확인 _수가 클때는 부적절
# 코딩은 10까지만 해놓음
def one_ten(number):
    for i in range(1, 10 + 1):
        if number % i != 0:
            return False
            break
    else:
        return True


number = 1

while not one_ten(number):
    number += 1
else:
    print(number)

# 2
# 두 수 사이의 최소공배수 구하는 함수/ (1,2)부터 ((1~19),20)까지
def 최소공배수(num1, num2):
    for i in range(1,min(num1,num2)+1)[::-1]:
        if (num1%i==0) and (num2%i==0):
            return int(num1*num2/i)
            break

while True:
    x = 1
    for i in range(2,20):
        x = 최소공배수(x,i)
    else:
        print(x)
        break

# others
lcm = 1
for check in (range(1, 21)):
    if lcm % check > 0:
        for lack in range(1, 21):
            if (lcm * lack) % check == 0:
                lcm *= lack
                break
print(lcm)
