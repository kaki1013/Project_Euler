prime = 28433 * (2 ** 7830457) + 1
mod = 10 ** 10
print(prime % mod)
print((pow(2, 7830457, mod) * 28433 + 1) % mod)