### ATTEMPT 1 ###

# import math
# from fractions import gcd

# limit = 100


# def isprime(n):
#     if not n % 2 and n > 2:
#         return False
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if not n % i:
#             return False
#     return True


# def relp(n):
#     counter = 0
#     for i in xrange(1, n):
#         if gcd(n, i) == 1:
#             counter += 1
#     return counter


def isperm(n, m):
    x = str(n)
    y = str(m)
    if len(x) != len(y):
        return False
    elif sorted(x) == sorted(y):
        return True
    return False

# primes = [x for x in xrange(3, 10000000 + 1, 2) if isprime(x)]
# # print primes
# print "primes table formulated"
# totient = []
# prod = 2
# for i in primes:
#     # print prod
#     prod *= i
#     if prod < limit:
#         totient.append(prod)
#     else:
#         break
# # print totient
# ans = 10000000
# blah = []
# for x in totient:
#     y = relp(x)
#     if isperm(x, y):
#         div = float(x) / float(y)
#         print div
#         if div < ans:
#             ans = div
#             print x, div

# # print blah
# # print relp(87109)
# # print isperm(123, 2134)

### ATTEMPT 2 ###

limit = 10000000
phi = [x for x in xrange(limit+1)]
ratio = limit
answer = 0
for x in xrange(2, limit+1):
    if phi[x] == x:
        for y in xrange(x, limit+1, x):
            phi[y] = phi[y] / x * (x - 1)

print "totient list formulated"
phi = phi[1:]
for i in xrange(2, limit+1):
    k = phi[i-1]
    if isperm(i, k):
        frac = float(i)/float(k)
        if frac < ratio:
            ratio = frac
            answer = i
            # print i, k, frac

print answer
