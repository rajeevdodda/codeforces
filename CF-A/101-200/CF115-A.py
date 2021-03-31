# https://codeforces.com/problemset/problem/115/A

n = int(input())
s = set()

for _ in range(n):
    s.add(input())

print(len(s))