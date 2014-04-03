import math


def isPrime(n):
    if not n % 2 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True


def primeFact(m):
    count = 0
    for i in range(2, m):
        if not m % i and isPrime(i):
            # print i
            count += 1
    return count

# print primeFact(465, 3)
# counter = 0
# while True:
#     counter += 1
#     if primeFact(counter) == 4 and primeFact(counter + 1) == 4:
#         if primeFact(counter + 2) == 4 and primeFact(counter + 3) == 4:
#             print counter, counter + 1, counter + 2, counter + 3
#             break
seq = 1
consec = 4
counter = 0

while consec != seq:
    counter += 1
    if primeFact(counter) == consec:
        seq += 1
    else:
        seq = 0
print counter
