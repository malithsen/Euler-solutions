for x in range(11, 100):
    for y in range(x + 1, 100):
        m = str(x)
        n = str(y)
        if m[1] == n[0]:
            if int(n[1]) != 0:
                if float(m[0]) / float(n[1]) == float(x) / float(y):
                    # print float(m[0]) / float(n[1]), "==", float(x) / float(y)
                    print x, y
# print float(11) / float(12)
