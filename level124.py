import math

def isprime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True

def factorprod(n):
    result = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if not n % i:
            if isprime(i):
                result.add(i)
                x = n//i
                if isprime(x):
                    result.add(x)
    # print result
    return reduce(lambda x,y: x*y, result)


ans = []
counter = 0
for i in range(1, 100001):
    counter += 1
    # print i
    fp = factorprod(i)
    ans.append([counter, fp])

res = sorted(ans, key=lambda l:l[1])

print res[9999][0]
# # print res[5]

# print factorprod(1024)