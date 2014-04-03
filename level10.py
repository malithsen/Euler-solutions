import math

limit = 2000000
ans = 0

def isprime(n):
    if not n%2 and n > 2:
        return False
    for i in xrange(3, int(math.sqrt(n)) +1, 2):
        if not n % i:
            return False
    return True
    
for i in xrange(2, limit+1):
    if isprime(i):
        ans += i
        
print ans
