numerator = [3, 7]
denominator = [2, 5]
for i in xrange(1000):
    numerator.append(numerator[-1] * 2 + numerator[-2])
    denominator.append(denominator[-1] * 2 + denominator[-2])

ans = 0
for i in xrange(1000):
    # print numerator[i], denominator[i]
    # print len(str(numerator[i])), len(str(denominator[i]))
    if len(str(numerator[i])) > len(str(denominator[i])):
        ans += 1

print ans