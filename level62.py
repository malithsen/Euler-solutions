def isPerm(x, y):
    if sorted(str(x)) == sorted(str(y)):
        return True
    else:
        False

cubes = [x ** 3 for x in range(1, 10000)]
# print cubes
for i in cubes:
    lst = []
    for j in cubes:
        # print i, j
        if isPerm(i, j):
            lst.append(j)
            # print lst
        if len(lst) >= 5:
            print lst
            break
