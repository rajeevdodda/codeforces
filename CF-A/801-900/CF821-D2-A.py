# https://codeforces.com/problemset/problem/821/A
import sys

lab = []
n = int(input())
for _ in range(n):
    lab.append(tuple(map(int, input().split())))
found = False
ans = 0
for i in range(n):
    for j in range(n):
        cell = lab[i][j]
        if cell == 1:
            ans += 1
            continue
        else:

            for k in range(n):
                for l in range(n):
                    if lab[i][k] + lab[l][j] == cell:
                        ans += 1
                        found = True
                        break
                if found:
                    break

print(ans)
if ans != n * n:
    print("NO")

else:
    print("YES")
