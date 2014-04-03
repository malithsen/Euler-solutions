import time

start = time.time()
 
ans = (28433 * pow(2, 7830457, 10**10) +1) % (10 ** 10)

elapsed = time.time() - start

print "Answer", ans
print "Time elapsed", elapsed
