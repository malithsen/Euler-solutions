limit = 500000
traian = set()
penta = set()
hexa = set()

for x in range(1, limit + 1):
    l = x * (x + 1) / 2
    traian.add(l)
for y in xrange(1, limit):
    m = y * (3 * y - 1) / 2
    penta.add(m)
for z in xrange(1, limit):
    n = z * (2 * z - 1)
    hexa.add(n)

traian.intersection_update(set(penta))
traian.intersection_update(set(hexa))
print traian
# print set(stage1.intersection_update(set(hexa)))
