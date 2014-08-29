b = 15
n = 21

target = 10**12

while n < target:
    x = 3 * b + 2 * n - 2
    y = 4 * b + 3 * n - 3

    b = x
    n = y

print b