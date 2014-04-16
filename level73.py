# from __future__ import division
from decimal import *
from fractions import gcd
from tqdm import *

LIMIT = 12001
high = Decimal(1)/Decimal(2)
low = Decimal(1)/Decimal(3)
answer = 0
# print low

for i in tqdm(xrange(1, LIMIT + 1)):
    for j in xrange(i+1, LIMIT + 1):
        if gcd(i, j) ==1:
            x = Decimal(i)/Decimal(j)
            if x < high and x > low:
                # print i, "/", j
                answer += 1

print answer