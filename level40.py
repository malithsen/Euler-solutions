LIMIT = 1000000
lst = ''
for i in xrange(1, LIMIT + 1):
    lst += str(i)

ans = int(lst[0]) * int(lst[9]) * int(lst[99]) * int(lst[999]) * int(lst[9999]) * int(lst[99999]) * int(lst[999999])
 
print ans

