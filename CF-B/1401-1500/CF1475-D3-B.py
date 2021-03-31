# https://codeforces.com/problemset/problem/1475/B

for _ in range(int(input())):
    n = int(input())
    total = n // 2020
    if total < 1:
        print("NO")
    else:
        new = n % 2020
        if total >= new:
            if n == (total - new) * 2020 + new * 2021:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
