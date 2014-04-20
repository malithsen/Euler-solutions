### ATTEMPT 1 ###

# from fractions import gcd
# from tqdm import *

# counter = 0
# for i in tqdm(range(1, 1000001)):
#     for j in range(1, i):
#         if gcd(i, j) == 1:
#             counter += 1
# print counter

### ATTEMPT 2 ###
# def farey(n):
#     a, b, c, d = 0, 1, 1, n
#     counter = -1
#     while c <= n:
#         k = int((n + b)/d)
#         a, b, c, d = c, d, k*c - a, k*d - b
#         counter += 1
#     print counter

# farey(1000000)

### ATTEMPT 3 ###
limit = 1000000
phi = [x for x in xrange(limit+1)]
result = 0
for x in xrange(2, limit+1):
    if phi[x] == x:
        for y in xrange(x, limit+1, x):
            phi[y] = phi[y] / x * (x - 1)
    result += phi[x]

print result
