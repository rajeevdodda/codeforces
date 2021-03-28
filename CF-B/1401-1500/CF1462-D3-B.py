# https://codeforces.com/problemset/problem/1462/B

for _ in range(int(input())):
    n = int(input())
    s = input()
    if s[:4] == "2020":
        print("YES")
    elif s[:3] + s[n - 1: n] == "2020":
        print("YES")
    elif s[:2] + s[n - 2:n] == "2020":
        print("YES")
    elif s[:1] + s[n - 3: n] == "2020":
        print("YES")
    elif s[n - 4: n] == "2020":
        print("YES")
    else:
        print("NO")
