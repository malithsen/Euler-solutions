import math

ans = 0
val = 0
nums = [x for x in range(1, 1001)]
for i in range(1, 100000):
    for j in nums[:]:
        z = float(math.sqrt(1 + j * (i ** 2)))
        # print z
        if i > z:
            break
        elif z.is_integer():
            print z, j, i
            del nums[nums.index(j)]
            if z > ans:
                val = j
                ans = z
print val
