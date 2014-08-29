import re

f = open('roman.txt').read()

lst1= ['DCCCC', 'VIIII']
lst2 = ['CCCC', 'XXXX', 'VXXX', 'IIII']
nums = map(str, f.split('\n'))

total = sum(len(x) for x in nums)
ans = 0

print total
for x in nums:
    total -= len(re.sub("DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII", 'yy', x))

print total