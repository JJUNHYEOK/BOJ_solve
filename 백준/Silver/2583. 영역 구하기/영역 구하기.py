import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int,input().split())
graph = [[0]*n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 1

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*n for _ in range(m)]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    global cnt

    cnt = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[ny][nx] and graph[ny][nx] == 0:
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((nx,ny))

    return cnt

area = []
count = 0

for y in range(m):
    for x in range(n):
        if graph[y][x] == 0 and not visited[y][x]:
            result = bfs(x,y)
            area.append(result)
            count += 1

area.sort()

print(count)
for data in area:
    print(data, end=" ")