import math

grid = int(raw_input("grid size :> "))
ans = math.factorial(2 * grid)/(math.factorial(grid)) ** 2
print ans
