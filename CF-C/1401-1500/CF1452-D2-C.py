# https://codeforces.com/problemset/problem/1452/C

for _ in range(int(input())):
    s = input()
    temp = set()
    a_open = 0
    b_open = 0
    ans = 0
    for i in s:
        if i == "[":
            a_open += 1
        elif i == "(":
            b_open += 1
        elif i == "]":
            if a_open:
                a_open -= 1
                ans += 1
        elif i == ")":
            if b_open:
                b_open -= 1
                ans += 1

    print(ans)
