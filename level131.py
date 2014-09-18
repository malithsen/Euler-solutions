import math

def isPrime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True

ans, p, i = 0, 0, 1

while p < 1000000:
    i += 1
    k = (i+1)**3 - i**3
    if isPrime(k):
        p = k
        ans += 1
print ans
