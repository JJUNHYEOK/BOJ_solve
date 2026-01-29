import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int,input().split())
world = [list(map(int,input().split())) for _ in range(n)]
home = []
chicken = []

for i in range(n):
    for j in range(n):

        if world[i][j] == 1:
            home.append((i,j))

        if world[i][j] == 2:
            chicken.append((i,j))

ans = 10**6

for val in combinations(chicken, m):
    total = 0
    for x1, y1 in home:
        num = 10**6
        for x2, y2 in val:
            num = min(num, abs(x1-x2)+abs(y1-y2))
        total += num
    
    ans = min(ans, total)

print(ans)
