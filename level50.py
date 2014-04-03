import math


def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True


# l = []
# length = 0
# for i in range(2, 1000):
#     if isprime(i):
#         l.append(i)
#         k = sum(l)

#         if k < 1000 and isprime(k):
#             length = len(l)
#             print k, length
primes = [x for x in range(2, 1000000) if isprime(x)]
counter = 0
maxlen = 0
print "prime table formulated"
# print sum(primes[:23])
for x in range(1, len(primes)):
    for y in range(x / 2):
        primesum = sum(primes[y:x])
        if isprime(primesum) and primesum < 1000000:
            if x - y + 2 > maxlen:
                print primesum, maxlen
                maxlen = x - y + 2
