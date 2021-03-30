# https://codeforces.com/problemset/problem/302/A

n, m = map(int, input().split())
negative = 0
positive = 0

array = input().split()

for i in array:
    if i == '1':
        positive += 1
    else:
        negative += 1

min_value = min(negative, positive)

for _ in range(m):
    l, r = map(int, input().split())
    diff = r - l + 1
    if diff % 2 == 1:
        print(0)
    else:
        if diff // 2 > min_value:
            print(0)
        else:
            print(1)
