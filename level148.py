import math

a = b = c = d = e = f = 0
result = 0
solved = False

i = 4
while not solved:
    a = i ** 2
    i += 1
    j = 3
    while (not solved) and j < i:
        c = j ** 2
        f = a - c
        if (f < 0) or (not math.sqrt(f).is_integer()):
            continue
        if j % 2:
            k = 1
        else:
            k = 2
        j += 1
        for num in xrange(k, j, 2):
            d = num ** 2
            e = a - d
            b = c - e
            if (b < 0) or (e < 0) or (not math.sqrt(b).is_integer()) or (not math.sqrt(e).is_integer()):
                continue
            x = (d + c) / 2
            y = (e + f) / 2
            z = (c - d) / 2
            result = x + y + z
            print result
            solved = True
            break