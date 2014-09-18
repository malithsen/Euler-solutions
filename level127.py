import math
from fractions import gcd
from tqdm import *

def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True

def factorprod(n):
    result = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if not n % i:
            x = n//i
            if isprime(x):
                result.add(x)
            if isprime(i):
                result.add(i)
                # if isprime(x):
                #     result.add(x)
    # print result
    return reduce(lambda x,y: x*y, result)

rad = {}
limit = 120000
ans = 0

for i in range(1, limit+1):
    rad[i] = factorprod(i)

for a in tqdm(range(1, limit)):
    for b in range(a+1, limit-a):
        if rad[a] * rad[b] * rad[a+b] >= a+b: continue
        if gcd(a, b) != 1: continue

        ans += a + b
print ans