import math

def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True


target = 2
# nums = range(1, target)
# print nums
primes = [x for x in range(2, 1000) if isprime(x)]
# print primes

while True:
    ways = [1] + [0] * target
    for prime in primes:
        for i in range(prime, target + 1):
            ways[i] += ways[i - prime]
    if ways[target] > 5000: break
    target += 1

print "Ans", ways[target], target