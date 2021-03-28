# https://codeforces.com/problemset/problem/1408/A

for _ in range(int(input())):
    n = int(input())
    a = tuple(input().split())
    b = tuple(input().split())
    c = tuple(input().split())
    print(a[0], end=" ")
    last = a[0]
    for i in range(1, n):
        if i % (n-1) == 0:
            if a[0] != a[i] and last != a[i]:
                print(a[i], end=" ")
                last = a[i]
            elif a[0] != b[i] and last != b[i]:
                print(b[i], end=" ")
                last = b[i]
            elif a[0] != c[i] and last != c[i]:
                print(c[i], end=" ")
                last = c[i]
        else:

            if a[i] != last:
                print(a[i], end=" ")
                last = a[i]
            else:
                print(b[i], end=" ")
                last = b[i]
    print()
# https://codeforces.com/problemset/problem/1480/A