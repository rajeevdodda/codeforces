# https://codeforces.com/problemset/problem/1475/A

for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        while True:
            n = n // 2
            if n % 2 == 0:
                continue
            else:
                if n == 1:
                    print("NO")
                    break
                else:
                    print("YES")
                    break


    else:
        print("YES")
