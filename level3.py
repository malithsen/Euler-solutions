import math

c = 0
number = 600851475143


def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True

while c < number:
    c += 1
    if not number % c:
        if isprime(c):
            print c
