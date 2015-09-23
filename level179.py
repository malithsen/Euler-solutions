limit = 10 ** 7
lst = [0] * limit
ans = 0

for i in range(2, limit//2):
    for j in range(2*i, limit, i):
        lst[j] += 1

for i in range(3, limit):
    if lst[i] == lst[i-1]:
        ans += 1

print ans

