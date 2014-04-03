p = 5  # power


def powerSum(n):
    return sum([pow(int(x), p) for x in list(str(n))])


def firstChar(n):
    return pow(int(str(n)[0]), p)

ans = 0
for i in range(20, 1000000):
    # print i
    if i == powerSum(i):
        ans += i
    # elif i < firstChar(i):
    #     print "break"
    #     break
# print firstChar(11)

print ans
