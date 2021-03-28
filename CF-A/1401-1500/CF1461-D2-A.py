# https://codeforces.com/problemset/problem/1461/A

for _ in range(int(input())):
    n, k = map(int, input().split())
    print("abc" * (n // 3) + "abc"[:(n % 3)])
