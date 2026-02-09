import sys

input = sys.stdin.readline

n = int(input())
tower = list(map(int,input().split()))

stk = []
result = []

for i in range(n):
    h = tower[i]

    while stk and stk[-1][0] < h:
        stk.pop()

    if not stk:
        result.append(0)
    else:
        result.append(stk[-1][1])

    stk.append((h, i+1))

print(*result)