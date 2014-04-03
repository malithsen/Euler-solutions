def p(n):
    target = n
    nums = range(1, target)
    # print nums
    ways = [1] + [0] * target

    for num in nums:
        for i in range(num, target + 1):
            ways[i] += ways[i - num]

    if not ways[target] + 1 % 1000000:
        return True

print p(10000)

