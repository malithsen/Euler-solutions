limit = 1000
k = 0
for l in range(0, limit):
    if not l%3 or not l%5:
        k += l
print k   
