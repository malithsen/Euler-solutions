limit = 10
x = 0
y = 1
ans = 0
a = 0
while a < 4000000:
    a = x + y
    x = y
    y = a
    if not a%2:
       ans += a

print ans
