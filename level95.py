import math


def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True


def factorSum(n):
    sumnum = 0
    for i in range(1, n/2 + 1):
        if not n % i:
            sumnum += i
    return sumnum


def chainLength(n):
    lst = [n]
    while True:
        l = factorSum(n)
        if l > 1000000:
            return [0, 0]
        if l not in lst:
            print l
            lst.append(l)
            n = l
        else:
            print lst, l
            return [len(lst[lst.index(l):]), lst[0]]
    # m = n
    # counter = 1
    # lowest = 1000000
    # while True:
    #     l = factorSum(m)
    #     print l
    #     if l > 1000000:
    #         return [0, 0]
    #     elif l < lowest:
    #         lowest = l
    #     elif l == n:
    #         return [counter, lowest]
    #     elif isprime(l) or l == m:
    #         # print "array"
    #         return [0, 0]
    #     else:
    #         m = l
    #         counter += 1

print chainLength(10040)
# print factorSum(562)
# print chainLength(12496)
# longest = 0
# chain = 0
# start = 0
# for i in xrange(9999, 20000):
#     # print i
#     k = chainLength(i)
#     # print k
#     if k[0] >= longest:
#         longest = k[0]
#         chain = k[1]
#         start = i
#         print longest, chain
# print "longest chain length", longest
# print "lowest in chain", chain
# print "starting value", start
