import math
limit = 100000


def triangular():
    for i in xrange(1, limit+1):
        x = i * (i + 1)/2
        l = []
        for j in xrange(1, int(math.sqrt(x) + 1)):
            if not x % j:
                l.append(x)
                if j < math.sqrt(x):
                    l.append(x//j)
                if len(l) > 500:
                    return x

print triangular()









