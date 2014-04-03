limit = 1000000
num = 0

for i in xrange(2, limit +1):
    lst = []
    lst.append(i)
    while i != 1:
        if not i%2:
            i = i/2
            lst.append(i)
        else:
            i = 3 * i + 1
            lst.append(i)
    if len(lst) > num:
        num = len(lst)       
        seq = lst[0]
        
print "max sequence", seq
print "length", num
