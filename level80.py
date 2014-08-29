from decimal import *

getcontext().prec = 101

def getDec(num):
    lst = str(Decimal(num).sqrt())
    lst = lst.replace('.', '0')[:-1]

    # print lst
    return sum(map(int, lst))

# print getDec(100)
print sum(getDec(i) for i in range(2, 100))
