# https://codeforces.com/problemset/problem/1440/A

for _ in range(int(input())):
    n, co, cl, h = map(int, input().split())
    s = input()
    zeros = 0
    ones = 0

    for i in s:
        if i == "0":
            zeros += 1
        else:
            ones += 1

    ans = min(((n * co) + (h * ones)), (( n * cl) + (h * zeros)),
              ((zeros * co) + (ones * cl)))
    print(ans)
