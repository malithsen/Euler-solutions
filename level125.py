import math
limit = 1000
sqlimit = int(math.sqrt(limit))
ans = set()


def ispalin(n):
    if len(n) == 1: return False
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
def ispali(n):
    x = str(n)
    # print list(x), list(reversed(x))
    if list(x) == list(reversed(x)):
        return True
    else:
        return False
counter = 0
for x in range(1, sqlimit):
    num = x ** 2
    for y in range(x+1, sqlimit):
        num += y ** 2
        if num > limit: break
        if ispalin(str(num)):
            counter += 1
            ans.add(num)

print sum(ans)

# print ispali(585)