limit = 1000

ans = 0
for i in range(1, limit + 1):
    a = i ** i
    ans += a
print str(ans)[-10:]  
