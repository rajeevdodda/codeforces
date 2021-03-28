# https://codeforces.com/problemset/problem/1481/A

for _ in range(int(input())):
    x, y = map(int, input().split())
    string = input()
    positiveX, positiveY, negativeX, negativeY = 0, 0, 0, 0
    for i in string:
        if i == "R":
            positiveX += 1
        elif i == "L":
            negativeX -= 1
        elif i == "U":
            positiveY += 1
        else:
            negativeY -= 1

    if negativeX <= x <= positiveX and negativeY <= y <= positiveY:
        print("YES")
    else:
        print("NO")
