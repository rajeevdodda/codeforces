# https://codeforces.com/problemset/problem/1445/A
t = int(input())
for k in range(t):
    n, x = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)
    b = sorted(map(int, input().split()))

    for i in range(n):
        if a[i] + b[i] > x:
            print("No")
            break
    else:
        print("Yes")
    if 0 <= k < t - 1:
        z = input()
