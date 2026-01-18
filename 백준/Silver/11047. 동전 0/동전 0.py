import sys

input = sys.stdin.readline

n, k = map(int,input().split())

money = []
cnt = 0

for _ in range(n):
    money.append(int(input()))

money.sort(reverse=True)

for cost in money:
    cnt += k // cost
    k %= cost

print(cnt)
