def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
num = [x for x in range(10)]
lst = []
for x in list(all_perms(num)):
    lst.append(int(''.join(map(str, x))))

lst = sorted(lst)
print lst[1000000 - 1]
