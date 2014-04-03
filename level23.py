#!/usr/bin/env python


LIMIT = 28123


def factors(n):
    faclist = []
    for i in range(1, int(n / 2) + 1):
        if not n % i:
            faclist.append(i)
    return sum(faclist)

abundant = []
sums = []
ans = 0
for x in xrange(1, LIMIT + 1):
    if factors(x) > x:
        abundant.append(x)
    if not any((x-a in abundant) for a in abundant):
        ans += x
print ans
