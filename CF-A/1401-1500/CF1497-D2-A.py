# https://codeforces.com/problemset/problem/1497/A

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    last = a[0]
    print(last, end=" ")
    other_stack = []
    for i in a[1:]:
        if i != last:
            print(i, end=" ")
            last = i
        else:
            other_stack.append(i)

    for i in other_stack:
        print(i, end=" ")
    print()
