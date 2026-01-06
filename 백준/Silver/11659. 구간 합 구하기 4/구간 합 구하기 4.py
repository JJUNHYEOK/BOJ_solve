import sys

input = sys.stdin.readline

n, m = map(int,input().split())
stk = list(map(int,input().split()))
mem = [0 for _ in range(n+1)]

for i in range(1, n+1):
    mem[i] = mem[i-1] + stk[i-1]

for _ in range(m):
    a, b = map(int,input().split())
    print(mem[b] - mem[a-1])


## 첫주부터 DP ..?