import math

limit = 50


def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True


primes = [x for x in range(2, limit + 1) if isprime(x)]

ans = prod = 1
for i in primes:
    # print prod
    prod *= i
    if prod < limit:
        ans = prod
        print ans
    else:
        break

print ans
