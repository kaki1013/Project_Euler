def 제곱의_합(x):
    sum_of_squares = 0
    for i in range(1,x+1):
        sum_of_squares+=i*i
    return sum_of_squares

def 합의_제곱(x):
    square_of_sum=0
    for i in range(1,x+1):
        square_of_sum+=i
    return square_of_sum**2

print(abs(제곱의_합(100)-합의_제곱(100)))

#others

# 1
a=0
b=0
for i in range(1,101):
    a+=i**2
for k in range(1,101):
    b+=k
b=b**2

print(abs(b-a))

# 2
first = 0
second = 0
for i in range(1,100+1):
    first += i
    second += i**2
print(first**2 - second)