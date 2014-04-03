def ispan(n):
    if sorted(n) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True

for i in xrange(9234, 9488):
    n = str(i) + str(2 * i)
    if ispan(n):
        print n