import math


def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True

oddComposite = []
primes = []
for x in range(2, 10000):
    if isprime(x):
        primes.append(x)
    elif x % 2 == 1:
        oddComposite.append(x)

for C in oddComposite:
    found = 0
    for P in primes:
        if P > C:
            break
        if math.sqrt((C - P)/2.0) % 1 == 0:
            found = 1
            break
    if found == 0:
        print C
        break
