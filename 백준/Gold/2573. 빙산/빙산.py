import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))


def melting():
    amount = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                sea = 0

                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if 0 <= ni < n and 0 <= nj < m:
                        if graph[ni][nj] == 0:
                            sea += 1

                amount[i][j] = sea

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                graph[i][j] -= amount[i][j]
                
                if graph[i][j] < 0:
                    graph[i][j] = 0

year = 0

while True:
    cnt = 0
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1

    if cnt == 0:
        print(0)
        break

    if cnt >= 2:
        print(year)
        break

    melting()
    year += 1