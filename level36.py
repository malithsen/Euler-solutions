import math

ans = 0


def isPali(n):
    if not len(n) % 2:
       #print "even"
        x = len(n) / 2
       #print n[:x] + " == " + n[x:][::-1]
        if n[:x] == n[x:][::-1]:
           #print n
            return True
    else:
       #print "odd"
        y = int(math.floor(len(n) / 2))
       #print y
       #print n[:y] + " == " + n[y + 1:][::-1]
        if n[:y] == n[y + 1:][::-1]:
            return True

print isPali('10001')
for i in xrange(1000000):
    bi = str(bin(i))[2:]
    if isPali(str(i)) and isPali(bi):
        print i, bi
        ans += i

print ans
