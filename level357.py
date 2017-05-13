import math

def isprime(n):
    if not n % 2  and n > 2: 
        return False
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if not n % i :
            return False
    return True

def is_prime_generating(n):
    return all((n % d != 0 or isprime(d + n // d)) for d in xrange(3, int(math.sqrt(n)) + 1, 2))

def calc():
    ans = 0
    for n in xrange(10**8 + 1):
        if isprime(n) and is_prime_generating(n):
            ans += n
            # print n
    return ans

print calc()