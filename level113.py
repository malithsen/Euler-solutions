from math import factorial

def nCr(n, r):
    return factorial(n)/(factorial(n-r) * factorial(r))

ans = (nCr(109, 100) - 1) + (nCr(110, 100) - 101) - 900
print ans

# algorithm http://melindalu.com/1hp/2013-02-07-project-euler-112-bouncy-numbers.html
