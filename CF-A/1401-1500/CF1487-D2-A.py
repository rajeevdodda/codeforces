# https://codeforces.com/problemset/problem/1487/A

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    ans = None
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            ans = i
            break

    if ans is None:
        print(0)
    else:
        print(n - (ans + 1))
