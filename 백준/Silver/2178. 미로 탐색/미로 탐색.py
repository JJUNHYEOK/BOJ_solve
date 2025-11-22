import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*m for _ in range(n)]
cnt = 0

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    dis = [[0]*m for _ in range(n)]
    dis[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and dis[nx][ny] == 0:
                    dis[nx][ny] = dis[x][y] + 1
                    q.append((nx,ny))

    
    return dis[n-1][m-1]

print(bfs(0,0))
