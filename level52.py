def equal(x, y):
    l = str(x)
    m = len(l)
    o = str(y)
    p = len(o)
    if m != p:
        return False
    counter = 0
    for num in l:
        if num in o:
            counter += 1
    if counter == p:
        return True

# print equal(125874, 25174)
for i in range(1, 1000000):
    a = 2 * i
    b = 3 * i
    c = 4 * i
    d = 5 * i
    e = 6 * i
    if equal(i, a):
        if equal(i, b):
            if equal(i, c):
                if equal(i, d):
                    if equal(i, e):
                        print i