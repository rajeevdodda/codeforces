# https://codeforces.com/problemset/problem/580/A

n = int(input())

a = tuple(map(int, input().split()))

length = 1

temp = 1
for i in range(1, n):
    if a[i - 1] - a[i] <= 0:
        temp += 1
    else:
        length = max(temp, length)
        temp = 1
length = max(temp, length)
print(length)
