import sys

input = sys.stdin.readline

n, m = map(int,input().split())
stk = list(map(int,input().split()))
stksum = [0 for _ in range(n+1)]

for i in range(1, n+1):
    stksum[i] = stksum[i-1] + stk[i-1]

for _ in range(m):
    a, b = map(int,input().split())
    print(stksum[b] - stksum[a-1])
