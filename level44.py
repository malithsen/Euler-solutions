import math


def penta(n):
    return n * (3 * n - 1) / 2


def isPent(n):
    x = (math.sqrt(24 * n + 1) + 1) / 6
    if x == int(x):
        return True
    else:
        return False


pentas = [penta(x) for x in xrange(1, 10000)]

for i in pentas:
    for j in pentas:
        x = i + j
        y = j - i
        # print x, y
        if x > 0 and y > 0:
            if isPent(x) and isPent(y):
                print i, j
                print "Ans", y
                break
