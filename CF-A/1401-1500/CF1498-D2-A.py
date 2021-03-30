# https://codeforces.com/problemset/problem/1498/A

import math

for _ in range(int(input())):
    n = int(input())
    while True:
        total = 0
        temp = n

        while temp > 0:
            total += temp % 10
            temp = temp // 10
        if math.gcd(n, total) == 1:
            n += 1
        else:
            print(n)
            break