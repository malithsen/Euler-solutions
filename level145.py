from tqdm import *

count = 0
even = ['0', '2', '4', '6', '8']


def pali(n):
    a = 0
    while n > 0:
        a = a * 10 + n % 10
        n = n / 10
    return a


def rev(num):
    for n in str(num):
        if n in even:
            return False
    return True

# print rev(409, 904)
# print pali(409)
for i in tqdm(xrange(1, 1000000000)):
    si = str(i)
    if si[-1] == '0':
        continue
    k = int(si[::-1])
    num = i + k
    if not num % 2:
        continue
    # k = pali(i)
    if rev(num):
        count += 1

print count
