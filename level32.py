def isPan(n):
    l = len(n)
    if l != 9:
        return False
    counter = 0
    for i in range(1, l + 1):
        if str(i) in list(n):
            counter += 1
        else:
            return False
    if counter == 9:
        return True
ans = set()
for x in xrange(1, 10000):
    for y in xrange(x, 10000):
        z = x * y
        num = str(x) + str(y) + str(z)
        if isPan(num):
            # print x, y, z
            # print num
            ans.add(int(z))
            # print "ans", ans
print sum(list(ans))
