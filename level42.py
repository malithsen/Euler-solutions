f = open('words42.txt')
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

trian = [int(0.5 * x * (x + 1)) for x in range(1, 20)]
# print trian


def value(word):
    count = 0
    for l in word:
        if not l == '\n':
            count += letters.index(l) + 1
    return count
# print value("SKY")

ans = 0
for x in f.readlines():
    if value(str(x)) in trian:
        ans += 1

print ans
