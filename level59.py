from collections import Counter

f = open('cypher.txt').read()

numlst = map(int, (f).split(','))
sublst = [[], [], []]
for i in range(len(numlst)):
    sublst[i%3].append(numlst[i])

# print Counter(sublst[1]).most_common(3), len(sublst[1])

def findKey():
    """Most commonly used letter in english is 'e', which accounts for like 12%"""
    key = ''
    for x in range(len(sublst)):
        asci = Counter(sublst[x]).most_common(2)[1][0]
        #Little hack to correct the second letter of the key
        if x == 1:
            asci = Counter(sublst[x]).most_common(3)[2][0]
        asci ^= ord('e')
        key += chr(asci)
    return key

def decrypt(lst):
    text = ''
    ans = 0
    key = findKey()
    for x in range(len(lst)):
        text += chr(lst[x] ^ ord(key[x%3]))
        ans += lst[x] ^ ord(key[x%3])
    print text
    return ans

print decrypt(numlst)
