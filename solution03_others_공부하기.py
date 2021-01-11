# 1 _중복되는 소인수 없다는 조건 필요
prime = 600851475143
num = 2
prime_list = []

while True:
    if prime == 1:
        break
    elif prime % num != 0:
        prime = prime
        num += 1
    else:
        prime = int(prime / num)
        prime_list.append(num)

print(max(prime_list))

# 2 _ 큰 소인수만 찾음
def big_prime(n) :
    p = 2
    while n != 1 :
        if n % p == 0 :
            n = n / p
        else:
            p = p + 1
    return p

print(big_prime(600851475143))

# 3 ??
def downfall(a):  #소수 판정기
    b=[]
    for i in range(2,a):
        if a%i==0:
            b.append(i)
    if b:
        return 2
    else:
        return a
d=[]
for k in range(1,100000):
    if 600851475143 % k == 0:
       d.append(downfall(k))
print(max(d))

#4
max = 600851475143
list = []
a= 2
while True:
    if max % a == 0:
        max /= a
        list.append(a)
    elif max <= 1: break
    else: a += 1
print(list.pop())

#5
a = 600851475143
b = 2
c = 0

while a>1:
    if a % b == 0:
        c = b
        a = a/b
        print(c)
    else:
        b += 1

#6
SOME=600851475143
while 1 :
    i=1
    while 1 :
        i=i+1
        if SOME % i == 0 :
            SOME=SOME/i
            break
    if SOME==1 :
        break
print(i)

#7: list를 전역으로 선언한 후, 재귀를 통해 소인수 하나씩 리스트에 더하였습니다.
list = []

def solve(N) :
    global list
    for i in range (2,N+1) :
        if N % i == 0 :
            if i not in list :
                list.append(i)
            solve(N//i)
            break
    return

solve(600851475143)
print(list)

#8
n=600851475143
k=2
result=2
while k<=n:
    while n%k==0:
        n=n//k
        result=k
    k=k+1
print(result)

#9
def split_num(res, n):
    if n == 1:
        return res
    for i in range(res, n + 1):
        if n % i == 0:
            if res < i:
                res = i
            k = n // i
            return split_num(res, k)

print(split_num(2, 600851475143))


#10
# 에라토스테네스의 체 알고리즘으로 다음 소수를 구한다
def SieveOfEratosthenes(primeNums):
    lastPrimeNum = primeNums[len(primeNums) - 1]
    num = lastPrimeNum + 1
    while True:
        isPrime = True

        # 시련의 시작 - 선대 소수들에게 나누어지면 죽음이다..
        for prime in primeNums:
            if num % prime == 0:
                isPrime = False

        # 이모든 시련을 통과하면 소수로 인정 받는다..!
        if isPrime == True:
            primeNums.append(num)
            break;
        num += 1


number = 600851475143
primeNums = [2]
while primeNums[len(primeNums) - 1] <= number:
    # 더이상 안나누어질때까지 계속 나눈다.
    if number % primeNums[len(primeNums) - 1] == 0:
        number = number / primeNums[len(primeNums) - 1]
    # 안나누어지면 다음 소수를 구한다.
    else:
        SieveOfEratosthenes(primeNums)
print(primeNums[len(primeNums) - 1])

#11
number = 600851475143
i = 2
divisionList = []

while (i <= number):
    if (number%i == 0):
        number = number/i
        print(str(number)+","+str(i))
        divisionList.append(i)
    else:
        i += 1

print(divisionList)