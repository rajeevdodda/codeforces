# https://codeforces.com/problemset/problem/96/A

s = input()

stack = None

count = 0

for i in s:
    if stack:
        if stack == i:
            count += 1
        else:
            stack = i
            count = 1
    else:
        stack = i
        count = 1

    if count == 7:
        print("YES")
        break

else:
    print("NO")
