a = "6963524437876961749120273824619538346438023188214475670667"
# from http://oeis.org/A113873/b113873.txt :(

ans = 0
for x in a:
    ans += int(x)
print ans