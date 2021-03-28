# https://codeforces.com/problemset/problem/1493/A

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(n - (k + 1) // 2)

    for i in range((k+1)//2, n + 1):
        if i == k:
            continue
        else:
            print(i , end=" ")
    print()
