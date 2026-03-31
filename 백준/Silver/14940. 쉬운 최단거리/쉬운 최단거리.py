import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*(m) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    g[r][c] = 0

    while q:
        
        x, y = q.popleft()

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if g[nx][ny] == 1:
                    if not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        g[nx][ny] = g[x][y] + 1


    return g

for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            sx, sy = i, j

ans = bfs(sx, sy)

for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and not visited[i][j]:
            g[i][j] = -1

jump = 0

for i in range(n):
    for num in ans[i]:
        jump += 1
        print(num, end=' ')

        if jump == len(ans[i]):
            print()
            jump = 0