lst = [0]
ans = 0
player1 = []
player2 = []

for i in range(1, 1001):
    lst.append((lst[-1]**2 + 45) % 1000000007)

# lst = [0, 45, 2070, 4284945]
lst = [1, 2, 10, 3]

for i in range(len(lst)):
    if i % 2:
        player2.append(lst[i])
    else:
        player1.append(lst[i])

player2.reverse()

i, j = 0, 0
for _ in range(len(player2)-1):
    print player2[j+1] - player1[i], player1[i+1] - player2[j]
    if player2[j+1] - player1[i] > player1[i+1] - player2[j]:
        ans += player1[i]
        i += 1
    else:
        ans += player2[j]
        j += 1
# ans += max(player1[i], player2[j])
print player1, player2
print ans