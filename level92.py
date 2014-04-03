LIMIT = 10000000
counter = 0

def process(n):
    while True:
        k = list(str(n))
        m = map(int, k)
        x = sum([pow(y, 2) for y in m])
        n = x
        if x == 89 or x == 1:
            return x
    
for i in xrange(1, LIMIT + 1):
    if process(i) == 89:
        counter += 1
        
print counter
        
    
