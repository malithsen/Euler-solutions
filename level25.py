limit = 10
x = 0
y = 1
ans = 0

for a in xrange(0, 10000):
    a = x + y
    x = y
    y = a
    if len(str(a)) == 1000:
        print a
