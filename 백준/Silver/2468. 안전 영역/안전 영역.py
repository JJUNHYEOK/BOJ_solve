import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

max_h = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] > max_h:
            max_h = graph[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > h and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))

ans = 0

for h in range(max_h+1):
    visited = [[False]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                bfs(i, j, h)
                cnt += 1

    
    ans = max(ans, cnt)

print(ans)