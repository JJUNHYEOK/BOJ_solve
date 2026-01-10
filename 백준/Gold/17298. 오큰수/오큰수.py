import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))

flag = [-1]*n
stk = []

for i in range(n):

    while stk and num[stk[-1]] < num[i]:
        idx = stk.pop()
        flag[idx] = num[i]
    stk.append(i)


print(*flag)
    