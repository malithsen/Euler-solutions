from decimal import *
getcontext().prec = 2000


def seqLen(lst):
    maxlen = len(lst) / 2
    length = 1
    for x in range(1, maxlen):
        if lst[0:x] == lst[x:2 * x]:
            if x > length:
                return x


def reci(n):
    temp = []
    y = str(Decimal(1)/Decimal(n))
    for x in y:
        temp.append(x)
    return temp[2:]


# seqLen(reci(983))
ans = 1
for num in range(1, 1000, 2):
    y = seqLen(reci(num))
    if y > ans:
        ans = y
        print num

print "Length of sequence", ans
