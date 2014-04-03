ans = 0

for i in xrange(1, 100):
    for j in xrange(1, 100):
        x = str(i ** j)
        if len(x) == j:

            ans += 1
print "Answer:", ans
