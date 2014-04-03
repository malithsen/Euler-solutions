import math

def match(n):
    s = str(n)
    return not all(int(s[x*2]) == x + 1 for x in range(9))

n = 138902663 #math.sqrt(19293949596979899)
while match(n ** 2):
    n -= 2
print n * 10