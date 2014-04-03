import math
from tqdm import *


def isPrime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True

def sqrtp(n):
    m = math.sqrt(n)
    if m.is_integer() and isPrime(m):
        return True

def primeFact(n):
    counter = 0
    ncount = 0
    for i in xrange(2, (n / 2) + 1):
        if not n % i:
            # print i
            counter += 1
            if counter > 2:
                return False
            if isPrime(i):
                ncount += 1
                if ncount > 2: return False
    if ncount == 2:
        return True

# print primeFact(8)
ans = 0
for i in tqdm(xrange(2, 10 ** 8 + 1)):
    if sqrtp(i):
        ans += 1
        continue
    if primeFact(i):
        ans += 1
print ans
# print sqrtp(9)