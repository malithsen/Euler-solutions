import math


def isPrime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True

primes = [x for x in range(2, 7071) if isPrime(x)]

print "Prime tables formulated"

ans = set()
limit = 50000000

for x in primes:
    sq = x ** 2
    if sq > limit:
        break
    else:
        for y in primes:
            cube = y ** 3
            sumsq = cube + sq
            if cube > limit:
                break
            elif sumsq > limit:
                break
            else:
                for z in primes:
                    frth = z ** 4
                    sumfrth = sumsq + frth
                    if frth > limit:
                        break
                    elif sumfrth > limit:
                        break
                    else:
                        # print "x: ", x, "y: ", y, "z: ", z
                        # print sumfrth
                        ans.add(sumfrth)
print "Answer", len(ans)
