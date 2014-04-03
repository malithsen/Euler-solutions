target = 100
nums = range(1, target)
# print nums
ways = [1] + [0] * target

for num in nums:
    for i in range(num, target + 1):
        ways[i] += ways[i - num]

print "Ans", ways[target]
