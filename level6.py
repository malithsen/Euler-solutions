limit = 100

def sq_sum():
    sq = 0
    for i in range(1, limit+1):
        sq += i ** 2
    return sq

def sum_sq():
    s = 0
    for i in range(1, limit+1):
        s += i
    s = s ** 2
    return s
         
ans = sum_sq() - sq_sum()
print ans
     
