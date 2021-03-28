# https://codeforces.com/problemset/problem/1506/A
import math

for _ in range(int(input())):
    n, m, x = map(int, input().split())
    if x % n == 0:
        row = n
    else:
        row = x % n

    column = math.ceil(x / n)

    print((row - 1) * m + column)
