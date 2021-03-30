# https://codeforces.com/problemset/problem/1459/A

for _ in range(int(input())):
    n = int(input())
    red = input()
    blue = input()
    red_count = blue_count = 0
    for i in range(n):
        if red[i] > blue[i]:
            red_count += 1
        elif red[i] < blue[i]:
            blue_count += 1

    if red_count > blue_count:
        print("RED")
    elif red_count < blue_count:
        print("BLUE")
    else:
        print("EQUAL")
