# https://codeforces.com/problemset/problem/802/G

s = input()
prev = 0
final = ""
for i in "heidi":
    temp = prev
    for j in s[prev:]:
        temp += 1
        if j == i:
            final += i
            prev = temp
            break

if final == "heidi":
    print("YES")
else:
    print("NO")


