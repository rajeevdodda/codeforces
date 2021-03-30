# https://codeforces.com/problemset/problem/1374/B

for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(0)
    elif n % 3 != 0:
        print(-1)
    else:
        step = 0

        while n % 3 == 0:
            if n % 2 == 0:
                n = n // 6
                step += 1
            else:
                n = n * 2
                step += 1
        if n == 1:
            print(step)
        else:
            print(-1)