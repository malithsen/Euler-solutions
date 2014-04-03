def area(tri):
    a, b, c = tri[0], tri[1], tri[2]
    a = abs((a[0] - c[0]) * (b[1] - a[1]) - ((a[0] - b[0]) * (c[1] - a[1])))
    return a # we dont need the actual area, besides division brings up floating
             # point issues.


counter = 0
with open('triangles.txt') as f:
    for line in f.readlines():
        line = line.split(',')
        cords = [[int(y) for y in line[x:x+2]] for x in range(0, len(line), 2)]
        x, y, z = cords[0], cords[1], cords[2]
        p = [0, 0]
        if area(cords) == area([x, y, p]) + area([x, z, p]) + area([z, y, p]):
            # print area(cords), area([x, y, p]), area([x, p, z]), area([p, y, z])
            counter += 1

print counter

# print area([[3, 0], [0, 4], [0, 0]])