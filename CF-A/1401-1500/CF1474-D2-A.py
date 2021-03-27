# https://codeforces.com/problemset/problem/1473/A

for _ in range(int(input())):
    n, d = map(int, input().split())
    a = tuple(map(int, input().split()))
    j, k = float("inf"), float("inf")
    is_greater = False
    for i in a:
        if i > d:
            is_greater = True
        if i < j:
            j, k = i, j
        elif i < k:
            k = i
    if is_greater:
        if j + k <= d:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")