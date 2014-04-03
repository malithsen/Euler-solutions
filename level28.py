limit = 1001 * 1001
counter = 1
add = 2
iteration = 0
ans = 0

for i in xrange(1, limit):
    if iteration < 4:
        iteration += 1
        # print iteration
        counter += add
        ans += counter
        if counter >= limit:
            break
    else:
        iteration = 0
        add += 2

print "Answer", ans + 1
