f = open('l13res.txt')

num = f.readlines()

lst = [int(x[:-1]) for x in num]
print sum(lst)
