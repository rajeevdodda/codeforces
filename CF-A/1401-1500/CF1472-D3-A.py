# https://codeforces.com/problemset/problem/1472/A

for _ in range(int(input())):
    w, h, n = map(int, input().split())
    area = w * h

    while w % 2 == 0:
        w = w // 2

    while h % 2 == 0:
        h = h // 2

    if area // (w * h) >= n:
        print("YES")
    else:
        print("NO")
