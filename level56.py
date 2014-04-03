ans = 0

for i in xrange(1, 100):
    for j in xrange(1, 100):
        x = i ** j
        lst = [int(y) for y in list(str(x))]
        k = sum(lst)
        if k > ans:
            ans = k
print ans
