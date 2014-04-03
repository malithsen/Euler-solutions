def isBouncy(n):
    n = str(n)
    counter = -1
    isInc = False
    isDec = False
    try:
        for m in n:
            counter += 1
            # print counter
            if int(n[counter + 1]) > int(m):
                isInc = True
            elif int(n[counter + 1]) < int(m):
                isDec = True
            if isDec and isInc:
                return True
    except:
        return False

count = 0
bcount = 0
for i in range(1, 5000000):
    count += 1
    if isBouncy(i):
        bcount += 1
        # print i
    if float(bcount) / float(count) == 0.99:
        print i, "Bouncy count", bcount
        break
# print isBouncy(134468)