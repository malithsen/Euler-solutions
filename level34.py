import math


def factosum(n):
    k = list(str(n))
    ans = [math.factorial(int(x)) for x in k]
    return sum(ans)

for i in range(3, 1000000):
    if factosum(i) == i:
        print i
