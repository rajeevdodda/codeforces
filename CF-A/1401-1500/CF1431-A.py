# https://codeforces.com/problemset/problem/1431/A

for _ in range(int(input())):
    n = int(input())
    customers = sorted(map(int, input().split()))
    cost = 0
    for i in range(n):
        cost = max(customers[i] * (n - i), cost)

    print(cost)
