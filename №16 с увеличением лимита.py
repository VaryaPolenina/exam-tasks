import sys
sys.setrecursionlimit(10**6)
def F(n):
    if n > 3000:
        return 1
    if n <= 3000 and n % 2 == 0:
        return F(n+1) - n + 1
    if n <= 3000 and n % 2 != 0:
        return F(n+2) - 2*n + 2
print(2 * F(39) - 2 * F(34))
