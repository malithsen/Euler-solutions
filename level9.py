import math

x = 1000
y = 1000

ans = 0
for a in range(1, x):
    for b in range(1, y):
        c = a ** 2 + b ** 2
      #  print a, b, math.sqrt(c)
        k = math.sqrt(c)
        if a + b + k == 1000:
            print a * b * k 
