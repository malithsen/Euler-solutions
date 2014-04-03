import math


def isPrime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True
primes = [x for x in range(2, 10000) if isPrime(x)]
seqlen = 0
amax = 0
bmax = 0

for b in range(1000):
    for a in range(-1000, 1000):
        # print a
        seq = 0
        for n in range(100):
            p = n * n + a * n + b
            if p in primes:
                seq += 1
            else:
                break
        # print seq
        if seq > seqlen:
            seqlen = seq
            amax = a
            bmax = b
print "seqlen", seqlen, "a", amax, "b", bmax
print "Answer", ama * bmax
