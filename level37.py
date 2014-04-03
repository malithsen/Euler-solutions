import math


def isPrime(n):
    if n == 1:
        return False
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True


def ltor(n):
    for i in range(len(n)):
        # print int(n[i:])
        if not isPrime(int(n[i:])):
            return False
    return True


def rtol(n):
    for i in range(len(n)):
        # print int(n[:i + 1])
        if not isPrime(int(n[:i + 1])):
            return False
    return True

# print rtol("11") and ltor("11")
# primes = [x for x in range(2, 20) if isPrime(x)]

counter = 0
num = 10
ans = 0

while counter != 11:
    x = str(num)
    num += 1
    if ltor(x) and rtol(x):
        print num - 1
        counter += 1
        ans += num - 1

print "Answer", ans