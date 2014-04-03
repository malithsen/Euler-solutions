import math


def maxlen(p):
    length = 0
    ans = 0
    counter = 0
    for x in range(1, p):
        for y in range(x, p):
            z = p - x - y
            if z != y:
                if z == math.sqrt(x ** 2 + y ** 2):
                    counter += 1
                    # print x, y, z
        if counter > length:
            length = counter
            ans = x
    return counter
# print maxlen(130)

leng = 0
ans = 0
for x in xrange(1, 1001):
    y = maxlen(x)
    if y > leng:
        leng = y
        ans = x
print "Ans", ans
