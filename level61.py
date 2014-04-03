tri = []
sq = []
pent = []
hexa = []
hept = []
octa = []


def generateLists():
    global tri, sq, pent, hexa, hept, pent
    limit = 100000
    n = 0
    i = 0

    while n < limit:
        i += 1
        n = i * (i+1)/2
        if len(str(n)) == 4:
            tri.append(n)
    n = 0
    i = 0
    while n < limit:
        i += 1
        n = i ** 2
        if len(str(n)) == 4:
            sq.append(n)
    n = 0
    i = 0
    while n < limit:
        i += 1
        n = i * (3 * i - 1)/2
        if len(str(n)) == 4:
            pent.append(n)
    n = 0
    i = 0
    while n < limit:
        i += 1
        n = i * (2 * i - 1)
        if len(str(n)) == 4:
            hexa.append(n)
    n = 0
    i = 0
    while n < limit:
        i += 1
        n = i * (5 * i - 3)/2
        if len(str(n)) == 4:
            hept.append(n)
    n = 0
    i = 0
    while n < limit:
        i += 1
        n = i * (3 * i - 2)
        if len(str(n)) == 4:
            octa.append(n)


def numType(n):
    if n in tri:
        return tri
    elif n in sq:
        return sq
    elif n in pent:
        return pent
    elif n in hexa:
        return hexa
    elif n in hept:
        return hept
    elif n in octa:
        return octa

generateLists()
biglist = tri + sq + pent + hexa + hept + octa

# if 8128 not in tri and 8128 not in pent:
#     print "works for sq"
for i in biglist:
    a = str(i)[2:]
    typ = numType(i)
    for j in biglist:
        b = str(j)[:2]
        if a == b and (j not in typ):
            c = str(j)[2:]
            typ2 = numType(j)
            typ = typ + typ2
            for k in biglist:
                d = str(k)[:2]
                # e = str(k)[2:]
                # f = str(i)[:2]
                if c == d and (k not in typ):
                    # print i, j, k
                    e = str(k)[2:]
                    typ3 = numType(k)
                    typ = typ + typ3
                    for l in biglist:
                        f = str(l)[:2]
                        # print "cccc"
                        if e == f and (l not in typ):
                            g = str(l)[2:]
                            typ4 = numType(l)
                            typ = typ + typ4
                            # print "bbbbb"
                            for m in biglist:
                                h = str(m)[:2]
                                if g == h and (m not in typ):
                                    x = str(m)[2:]
                                    typ5 = numType(m)
                                    typ = typ + typ5
                                    # print "aaaaa"
                                    for n in biglist:
                                        y = str(n)[:2]
                                        if x == y:
                                            # print "ddddd"
                                            z = str(n)[2:]
                                            zz = str(i)[:2]
                                            # print i, j, k, l, m, n
                                            if z == zz:
                                                print i+j+k+l+m+n
