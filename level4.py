x = 1000
y = 1000

ans = 0
for a in range(1, x):
    for b in range(1, y):
        k = str(a * b)
        x = len(k)/2
        if k[:x] == k[x:][::-1]:
            j = int(k)
            if j > ans:
               ans = j
print ans     
