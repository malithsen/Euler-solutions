f = open('l8res.txt')
lst = list(f.read())

lst = [x for x in lst if x.isdigit()]

ans = 0
for i,t in enumerate(lst):
    k = int(lst[i]) * int(lst[i+1]) * int(lst[i+2]) * int(lst[i+3]) * int(lst[i+4]) 

    if k > ans:
        ans = k
        print ans

        

