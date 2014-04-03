from munkres import Munkres, print_matrix
import sys

# matrix = [7, 53, 183, 439, 863,
#           497, 383, 563, 79, 973,
#           287, 63, 343, 169, 583,
#           627, 343, 773, 959, 943,
#           767, 473, 103, 699, 303]

# def getMax(row):
#     return [max(row), row.index(max(row))]

matrix = [7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583,
          627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913,
          447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743,
          217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350,
          960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350,
          870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803,
          973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326,
          322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973,
          445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848,
          414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198,
          184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390,
          821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574,
          34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699,
          815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107,
          813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805]
def rowify(mat, length):
    chunks = [mat[x:x+length] for x in xrange(0, len(mat), length)]
    return chunks
matrix = rowify(matrix, 15)
# def rmcol(mat, n):
#     for x in mat:
#         x.pop(n)
#     return mat

# nm = rowify(matrix, 5)
# print nm
# # print rmcol(nm, 2)
# ans = 0
# for i in xrange(5):
#     gm = getMax(nm[i])
#     ans += gm[0]
#     print gm[0]
#     rmcol(nm, gm[1])
# print ans

# matrix = [[5, 9, 1],
#           [10, 3, 2],
#           [8, 7, 4]]

### Hungarian algorithm ###
cost_matrix = []
for row in matrix:
    cost_row = []
    for col in row:
        cost_row += [sys.maxint - col]
    cost_matrix += [cost_row]

m = Munkres()
indexes = m.compute(cost_matrix)
print_matrix(matrix, msg='Lowest cost through this matrix:')
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print '(%d, %d) -> %d' % (row, column, value)

print 'total profit=%d' % total