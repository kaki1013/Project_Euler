#1_1 집합은 중복원소가 없음을 이용
threes=list(range(0,1000,3))
fives=list(range(0,1000,5))

a=set(threes+fives)

print(sum(a))

#1_2
print(sum(set(list(range(0,1000,3))+list(range(0,1000,5)))))

#2_1 1부터 1000까지 순회하며 판단하여 합산_for
total=0

for i in range(1,1000):
    if i%3==0 or i%5==0:
        total+=i

print(total)

#2_2 1부터 1000까지 순회하며 판단하여 합산_while
total=0
i=0

while i<1000:
    if i%3==0 or i%5==0:
        total+=i
    i+=1

print(total)