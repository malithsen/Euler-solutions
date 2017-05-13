# matrix =[
#         [131, 673, 234, 103,  18],
#         [201,  96, 342, 965, 150],
#         [630, 803, 746, 422, 111],
#         [537, 699, 497, 121, 956],
#         [805, 732, 524,  37, 331]
24#         ]

def main(matrix):
    size = len(matrix)
    best = [matrix[row][0] for row in range(size)]

    for col in range(1, size):
        column = [matrix[row][col] for row in range(size)]

        temp = column[:]

        for x in range(size):
            column[x] += best[x]

            for y in range(0, x):
                cell = sum([best[y]]+temp[y:x+1])
                if cell < column[x]:
                    column[x] = cell

            for z in range(x, size):
                cell = sum([best[z]] + temp[x:z+1])
                if cell < column[x]:
                    column[x] = cell

        best = column
    return min(best)
matrix = []
with open('matrix.txt') as f:
    for line in f:
        row = [int(x) for x in line.split(',')]
        matrix.append(row)

print main(matrix)
