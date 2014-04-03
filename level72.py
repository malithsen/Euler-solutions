from fractions import gcd
from tqdm import *

counter = 0
for i in tqdm(range(1, 1000001)):
    for j in range(1, i):
        if gcd(i, j) == 1:
            counter += 1
print counter
