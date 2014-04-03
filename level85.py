lim = mindiff = 2000000

for x in range(2, 101):
    for y in range(x, 101):
        diff = abs((x*(x + 1) * y*(y + 1))/4 - lim)
        if diff < mindiff:
            mindiff = diff
            ans = x * y
print ans