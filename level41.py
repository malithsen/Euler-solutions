import math


def isPan(n):
    m = str(n)
    l = len(m)
    counter = 0
    for i in range(1, l + 1):
        if str(i) in list(m):
            counter += 1
        else:
            return False
    if counter == l:
        return True


def isPrime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if not n % i:
            return False
    return True

# print isPan(2143)
for x in xrange(1, 999999999):
    if isPan(x) and isPrime(x):
        print x
