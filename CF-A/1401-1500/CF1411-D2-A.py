# https://codeforces.com/problemset/problem/1411/A

for _ in range(int(input())):
    n = int(input())
    s = input()
    back = 0

    for i in range(n - 1, -1, -1):
        if s[i] == ")":
            back += 1
        else:
            break

    if back > (n - back):
        print("YES")
    else:
        print("NO")

