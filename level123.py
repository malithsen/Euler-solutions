from math import sqrt
primespos = 0
def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True

def calc(n):
    x = primespos
    y = pow((n - 1), x) + pow((n + 1), x)
    z = y % (pow(n, 2))
    # print z
    return z

primes = [x for x in xrange(10000000) if isprime(x)][2:]
print "Prime list formulated", len(primes)
# print primes
limit = pow(10, 10)
for x in primes:
    primespos += 1
    if calc(x) > limit:
        print primespos
        break
