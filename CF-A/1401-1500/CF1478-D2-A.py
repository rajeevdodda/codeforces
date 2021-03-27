# https://codeforces.com/problemset/problem/1478/A

for _ in range(int(input())):
    n = int(input())
    hash_map = {}
    ans = 0
    colors = map(int, input().split())
    for i in colors:
        hash_map[i] = hash_map.get(i, 0) + 1
        ans = max(ans, hash_map[i])

    print(ans)
