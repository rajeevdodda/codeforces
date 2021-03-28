# https://codeforces.com/problemset/problem/1452/A

for _ in range(int(input())):
    x, y = map(int, input().split())
    if abs(x - y) <= 1:
        print(x + y)
    else:
        print(3 + ((max(x, y)) - 2) * 2)
