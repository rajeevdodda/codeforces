# https://codeforces.com/problemset/problem/337/A

n, m = map(int, input().split())

puzzles = sorted(map(int, input().split()))
i = 0
ans = float("inf")
while i + n <= m:
    ans = min(ans, puzzles[i + n - 1] - puzzles[i])
    i += 1

print(ans)
