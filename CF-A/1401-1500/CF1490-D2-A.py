# https://codeforces.com/problemset/problem/1490/A
import math

for _ in range(int(input())):
    n = int(input())
    arr = tuple(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        a, b = max(arr[i], arr[i - 1]), min(arr[i], arr[i - 1])
        if a / b <= 2:
            continue
        else:
            while a / b > 2:
                a = math.ceil(a / 2)
                ans += 1
    print(ans)
