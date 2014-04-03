import operator as op


def ncr(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer // denom

# print ncr(99, 10)
ans = 0
for i in range(1, 101):
    for j in range(1, i):
        # print i, j
        if ncr(i, j) > 1000000:
            ans += 1
print "Ans", ans
