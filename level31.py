############## INCOMPLETE ####################

import math
from itertools import permutations


def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True

x = 100
y = 50
z = 20
a = 10
b = 5
c = 2
d = 1
count = 0
for i in xrange(3):
    if i * x > 200:
        break
    for j in xrange(5):
        if i * x + j * y > 200:
            break
        for k in xrange(11):
            if i * x + j * y + z * k > 200:
                break
            for l in xrange(21):
                if i * x + j * y + z * k + l * a > 200:
                    break
                for m in xrange(41):
                    if i * x + j * y + z * k + l * a + m * b > 200:
                        break
                    for n in xrange(101):
                        if i * x + j * y + z * k + l * a + m * b + n * c > 200:
                            break
                        for o in xrange(201):
                            if i * x + j * y + z * k + l * a + m * b + n * c + o * d == 200:
                                # print i, "*", x, ",", j, "*", y, ",", k, "*", z
                                count += 1
print count + 1
