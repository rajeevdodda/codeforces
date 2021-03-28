# https://codeforces.com/problemset/problem/1492/A
import math
from decimal import Decimal

for _ in range(int(input())):
    p, a, b, c = map(int, input().split())
    if p >= a:
        amin = abs(p - math.ceil(Decimal(p) / Decimal(a)) * a)
    else:
        amin = a - p

    if p >= b:
        bmin = abs(p - math.ceil(Decimal(p) / Decimal(b)) * b)
    else:
        bmin = b - p

    if p >= c:
        cmin = abs(p - math.ceil(Decimal(p) / Decimal(c)) * c)
    else:
        cmin = c - p

    print(min(amin, bmin, cmin))