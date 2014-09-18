# vals = [1, 3, 7]

# def gen(n):
#     global vals

#     # if n <= 4:
#     #     return vals[n-1]
#     for i in range(2, n):
#         newVal = 3 * vals[-1] - 2 * vals[-2]
#         vals.append(newVal)
#     print vals
#     return vals[-1]

# print gen(4)
#Oh fuck it
#https://oeis.org/A051389
a = [1, 2, 4, 8, 20, 42,102, 250, 610, 1486,3710, 9228, 23050, 57718,145288, 365820, 922194, 2327914]
print sum(a)