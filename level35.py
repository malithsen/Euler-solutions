import math


def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True


def numbers(num):
    num = list(str(num))
    l = []
    for i in num:
        k = num.pop(0)
        num.append(k)
        l.append(int(''.join(num)))
    return l

counter = 0
for n in range(2, 1000000):
    if all(isprime(i) for i in numbers(n)):
        counter += 1
print counter
