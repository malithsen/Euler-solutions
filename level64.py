import math


ans = 0

for x in range(2, 10001):
    r = limit = int(math.sqrt(x))
    if limit * limit == x:
        continue
    k = 1
    period = 0
    while k != 1 or period == 0:
        k = (x - r * r) / k
        r = ((limit + r) / k) * k - r
        period += 1
    if period % 2 == 1:
        ans += 1

print "Answer", ans