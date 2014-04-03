from itertools import *

def is_dev(digits):
    primes = [1, 2, 3, 5, 7, 11, 13, 17]
    for i in range(1, len(digits)-2):
        if int(''.join(digits[i:i+3])) % primes[i]:
            return False
    return True

def list_to_int(lst):
    return int(''.join(str(i) for i in lst))

# print list_to_int(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
ans = 0
pandi = list(permutations((str(i)) for i in range(10)))
print len(pandi)
for n in pandi:
    # print n
    # break
    if is_dev(n):
        m = list_to_int(n)
        print m
        ans += m
print "Ans", ans