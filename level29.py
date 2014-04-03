ans = set()

limit = 100
for x in xrange(2, limit + 1):
    for y in xrange(2, limit + 1):
        ans.add(x ** y)
lst = sorted(list(ans))
print len(lst)
