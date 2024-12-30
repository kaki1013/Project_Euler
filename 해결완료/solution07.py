# 10001번째 소수찾기
primes=[2]
x=1

while len(primes)<10002:
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
           break
    else:
        primes.append(x)
    x+=2

print(primes[-1])