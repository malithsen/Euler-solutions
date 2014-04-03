import math


def factosum(n):
    k = list(str(n))
    ans = [math.factorial(int(x)) for x in k]
    return sum(ans)

# for i in range(3, 1000000):
#     if factosum(i) == i:
#         print i


def chain(n):
    count = []
    while True:
        m = factosum(n)
        # print m
        if m not in count:
            count.append(m)
            n = m
        else:
            break
    if len(count) + 1 == 60:
        return True
    else:
        return False

# print chain(42)
ans = 0
for x in xrange(1, 1000000):
    if chain(x):
        ans += 1
        print ans
print "Ans", ans
