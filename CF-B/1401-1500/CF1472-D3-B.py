# https://codeforces.com/problemset/problem/1472/B

for _ in range(int(input())):
    n = int(input())
    candies = input().split()
    alice = 0
    bob = 0
    for i in candies:
        if i == "1":
            alice += 1
        else:
            bob += 1
    if alice % 2 == 1:
        print("NO")
    else:
        if alice == 0:
            if bob % 2 == 1:
                print("NO")
            else:
                print("YES")
        else:
            print("YES")

