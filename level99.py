import math

a = 519432
b = 525806
with open("base_exp.txt") as f:
    lst = f.readlines()
    for i, j in enumerate(lst):
        # print int(j)
        k = j.index(",")
        c = int(j[:k])
        d = int(j[k+1:-1])
        if (float(b) / float(d)) < float(math.log(c, 10) / math.log(a, 10)):
            print "line", i+1, "nums", c, d
            print float(b / d), "<", float(math.log(c, 10) / math.log(a, 10))
            a = c
            b = d