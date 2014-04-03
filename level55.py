import math


def isPalin(n):
    n = str(n)
    if not len(n) % 2:
        x = len(n) / 2
        if n[:x] == n[x:][::-1]:
            return True
    else:
        y = int(math.floor(len(n) / 2))
        if n[:y] == n[y + 1:][::-1]:
            return True


def getRev(n):
    return int(str(n)[::-1])


def isLycheral(n):
    counter = 0
    i = n
    while counter < 50:
        counter += 1
        j = getRev(i)
        if isPalin(i + j):
            return False
        else:
            i = i + j
    # print counter
    return True
# print isLycheral(4994)

ans = 0
for x in xrange(1, 10000):
    if isLycheral(x):
        ans += 1

print ans
