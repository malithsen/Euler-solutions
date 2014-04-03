nums = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
teens = [6, 6, 5, 5, 5, 7, 6, 6]

LIMIT = 5
tot = 0


def digit():
    ans = 0
    for i in range(1, 10):
        ans += nums[i]
    return ans


def teensum():
    ans = 70 + digit()
    for i in teens:
        ans += (i * digit())
        ans += 46
        # print i * digit()
    return ans


def hundsum():
    ans = teensum()
    for i in range(1, 10):
        ans += nums[i] + 10 + teensum()
        # ans += nums[i] + 7
    return ans
# print digit()
print teensum()
print hundsum() + 11
