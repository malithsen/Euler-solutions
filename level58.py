import math

limit = 1001 * 1001 * 100 * 10
counter = 1
add = 2
iteration = 0
primecount = 0
diagonals = 1


def isPrime(n):
    if n == 1:
        return False
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True


for i in xrange(1, limit):
    if iteration < 4:
        iteration += 1
        # print counter, primecount, diagonals
        # print iteration
        counter += add
        if isPrime(counter):
            primecount += 1
        if float(primecount) / float(diagonals) <= 0.1:
            print primecount, diagonals
            print math.sqrt(counter - add)
            break
        if counter >= limit:
            break
    else:
        iteration = 0
        diagonals += 4
        add += 2

# print "Answer", ans + 1
