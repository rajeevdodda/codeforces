# https://codeforces.com/problemset/problem/1447/A
for _ in range(int(input())):
    n = int(input())
    print(n - 1)
    print(*range(n, 1, -1))
