def prime_test(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
            break
    else:
        return True

def prime_factorization(number):
    prime_factors = []
    while not prime_test(number):
        for i in range(2, int(number ** 0.5)+1):
            if number % i == 0:
                prime_factors.append(i)
                number /= i
                break
    else:
        prime_factors.append(int(number))
        print(prime_factors)

prime_factorization(600851475143)


# 함수 하나로 합침
def prime_factorization_upgrade(number):
    prime_factors=[]
    for j in range(2, int(number ** 0.5) + 1):
        if number % j == 0:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    prime_factors.append(i)
                    number /= i
                    break
    else:
        prime_factors.append(int(number))
        print(prime_factors)

prime_factorization_upgrade(600851475143)