# https://codeforces.com/problemset/problem/1466/B

for _ in range(int(input())):
    n = int(input())
    s = set()
    notes = map(int, input().split())
    for i in notes:
        if i not in s:
            s.add(i)
        else:
            s.add(i + 1)

    print(len(s))
