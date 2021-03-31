# https://codeforces.com/problemset/problem/1341/A

for _ in range(int(input())):
    n, a, b, c, d = map(int, input().split())

    min_gram = a - b
    max_gram = a + b
    min_w = c - d
    max_w = c + d

    if min_w <= n * min_gram or n * max_gram <= max_w:
        print("YES")
    else:
        print("NO")
