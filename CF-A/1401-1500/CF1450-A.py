# https://codeforces.com/problemset/problem/1450/A

for _ in range(int(input())):
    n = int(input())
    s = input()
    b = ""
    ans = ""
    for i in s:
        if i == "b":
            b += "b"
        else:
            ans += i

    print(b + ans)