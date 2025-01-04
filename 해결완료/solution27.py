def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def get_score(a, b):
    count = 0
    while 1:
        check = count*count + a*count + b
        if check <= 0:
            break
        if not is_prime(check):
            break
        count += 1
    return count


ans = []
max_score = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        score = get_score(a, b)
        if score > max_score:
            ans = [(a, b)]
            max_score = score
        elif score == max_score:
            ans.append((a, b))

if len(ans) == 1:
    a, b = ans[0]
    print(a*b, max_score)
else:
    print(ans)
