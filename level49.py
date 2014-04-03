from itertools import permutations
import math


def isPerm(x, y, z):
    if x == y == z:
        return False
    m = list(permutations(list(str(x))))
    n = tuple(str(y))
    o = tuple(str(z))
    # print list(m), n, o
    if n not in m:
        return False
    if o not in m:
        return False
    if n in m and o in m:
        return True


def isPrime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True


primes = [x for x in range(999, 10000) if isPrime(x)]
# perms = []
print len(primes)
for x in primes:
    for y in primes[primes.index(x) + 1:]:
        z = 2 * y - x
        if z in primes:
            if isPerm(x, y, z):
                print "ans", x, y, z
# for n in perms:
#     for m in perms:
#         for o in perms:
#             if m - n == o - m and m != n:
#                 print m, n, o
# print perms
# print isPerm(123, 213, 321)
# print isPrime(9335)
