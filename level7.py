import math

limit = 6
c = 0

def isprime(n):
    if not n % 2 and n> 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True
    
for i in xrange(2, 115000):
     if isprime(i):
         c += 1
         print str(c) + 'th prime', i 
         

