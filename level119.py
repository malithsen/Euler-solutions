def sumNum(n):
    r = 0
    while n:
        r, n = r + n % 10, n / 10
    return r


def power(n):
    i = 2
    while i < 100:
        x = n ** i
        # print x, i
        # if n > sumNum(x):
        #     return False
        if n == sumNum(x):
            return x
        i += 1

# print power(17)
lst = []
for i in xrange(5, 100):
    x = power(i)
    if x:
        lst.append(x)
print (sorted(lst))[19]
# counter = 0
# for i in xrange(1, 100000000):
#     # print i
#     if  power(i):
#         counter += 1
#         print counter, i