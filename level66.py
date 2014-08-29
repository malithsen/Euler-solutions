# Solution to Pell's equation as explained in http://www.had2know.com/academics/pell-equation-calculator.html

import math
from fractions import Fraction

def isSqrt(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    return False

def cf(n):
    """ Compute the continued fraction representation of the
        square root of N.

        The first element in the returned array is the whole
        part of the fraction. The others are the denominators
        up to (and not including) the point where it starts
        repeating.

        Uses the algorithm explained here:
        http://www.mcs.surrey.ac.uk/Personal/R.Knott/Fibonacci/cfINTRO.html
        In the section named: "Methods of finding continued
        fractions for square roots"
    """
    if isSqrt(n):
        return [int(math.sqrt(n))]

    ans = []

    step1_num = 0
    step1_denom = 1

    while True:
        nextn = int((math.floor(math.sqrt(n)) + step1_num) / step1_denom)
        ans.append(int(nextn))

        step2_num = step1_denom
        step2_denom = step1_num - step1_denom * nextn

        step3_denom = (n - step2_denom ** 2) / step2_num
        step3_num = -step2_denom

        if step3_denom == 1:
            ans.append(ans[0] * 2)
            break

        # print 'looping'
        step1_num, step1_denom = step3_num, step3_denom

    return ans


def fracSum(lst):
    lst.pop()
    lst.reverse()
    #ugly hack
    if not len(lst) % 2:
        return 0
    return reduce(lambda x, y: Fraction(1, x) + Fraction(y), lst)


# print cf(7)
# print fracSum([4, 1, 3, 1, 8])
# print fracSum(cf(661))
# print fracSum(cf(991))

nums = [x for x in range(10, 1001) if not isSqrt(x)]

ans = []
for num in nums:
    ans.append([num, fracSum(cf(num)).numerator])

print max(ans, key=lambda x:x[1])
