# https://codeforces.com/problemset/problem/1491/A

n, q = map(int, input().split())
arr = list(map(int, input().split()))

zeros = 0
ones = 0

for i in arr:
    if i == 0:
        zeros += 1
    else:
        ones += 1
for _ in range(q):
    x, k = map(int, input().split())
    if x == 1:
        if arr[k - 1] == 0:
            arr[k - 1] = 1
            zeros -= 1
            ones += 1
        else:
            arr[k - 1] = 0
            zeros += 1
            ones -= 1
    else:
        if k <= ones:
            print(1)
        else:
            print(0)
