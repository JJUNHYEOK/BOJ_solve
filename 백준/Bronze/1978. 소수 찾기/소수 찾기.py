import sys

input = sys.stdin.readline

n = int(input())
cnt = 0

arr = list(map(int,input().split()))

for val in arr:

    if val < 2:
        continue

    for i in range(2, val):
        if val%i == 0:
            break
    else:
        cnt += 1

print(cnt)
