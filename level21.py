ans = set([])


def factorSum(n):
    sumnum = 0
    for i in range(1, n):
        if not n % i:
            sumnum += i
    return sumnum

for num in range(1, 10000):
    x = factorSum(num)
    if num == factorSum(x):
        if num != x:
            ans.add(num)

print sum(ans)
