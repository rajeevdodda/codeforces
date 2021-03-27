# https://codeforces.com/problemset/problem/1462/A

for _ in range(int(input())):
    n = int(input())
    numbers = tuple(map(int, input().split()))
    first = 0
    last = n - 1

    while first < last:
        print(numbers[first], end=" ")
        print(numbers[last],  end=" ")
        first += 1
        last -= 1

    if n % 2 == 1:
        print(numbers[first])
    else:
        print()
