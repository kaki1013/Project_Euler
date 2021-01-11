# 3자리 수 2개의 곱 집합과 5자리, 6자리 회문수 집합의 교집합 구하기

# 3자리 수 2개의 곱 목록_227521개(중복X)
the_product_of_two_3_digit_numbers = []

for i in range(100, 1000):
    for j in range(100, 1000):
        the_product_of_two_3_digit_numbers.append(i * j)

the_product_of_two_3_digit_numbers = set(the_product_of_two_3_digit_numbers)

# 5자리 회문수 집합 : 10000a+1000b+100c+10b+a=10001a+1010b+100c
# 사실 최대 찾는 문제라 필요 없음
five_digit_palindrome=[]

for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            five_digit_palindrome.append(10001*a+1010*b+100*c)

five_digit_palindrome = set(five_digit_palindrome)

# 6자리 회문수 집합 : 100000a+10000b+1000c+100c+10b+a=100001a+10010b+1100c=11(9091a+910b+100c)
six_digit_palindrome=[]

for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            six_digit_palindrome.append(100001*a+10010*b+1100*c)

six_digit_palindrome = set(six_digit_palindrome)

# 2개의 3자리수의 곱이면서 회문수인 수들의 집합
palindrome_made_from_the_product_of_two_3_digit_numbers\
    =(the_product_of_two_3_digit_numbers&five_digit_palindrome)|\
     (the_product_of_two_3_digit_numbers&six_digit_palindrome)

# 최대인 수 찾기
print(max(list(palindrome_made_from_the_product_of_two_3_digit_numbers)))