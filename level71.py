from fractions import gcd


for i in range(428500, 429000):
    for j in range(999900, 1000001):
        if gcd(i, j) == 1:
            z = float(i) / float(j)
            if z < float(3) / float(7):
                print i, j