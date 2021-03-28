# https://codeforces.com/problemset/problem/1453/A

for _ in range(int(input())):
    n, m = map(int, input().split())
    nt = tuple(map(int, input().split()))
    mt = tuple(map(int, input().split()))

    i, j = 0, 0
    ans = 0
    while i < n and j < m:
        if nt[i] == mt[j]:
            ans += 1
            j += 1
            i += 1
        elif nt[i] < mt[j]:
           i += 1
        else:
            j += 1

    print(ans)