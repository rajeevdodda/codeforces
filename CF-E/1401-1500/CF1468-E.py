# https://codeforces.com/problemset/problem/1468/E

for _ in range(int(input())):
    lengths = sorted(map(int, input().split()))
    print(lengths[0] * lengths[2])