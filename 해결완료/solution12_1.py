# 23.585715s
def triangle_number(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

def factors(n):
    factor_list=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            factor_list.append(i)
            factor_list.append(n//i)
    return factor_list

i=1

while len(factors(triangle_number(i)))<500:
    i+=1
print(triangle_number(i))