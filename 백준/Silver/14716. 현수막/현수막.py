import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]
cnt = 0

dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True
    global cnt

    while q:
        x, y = q.popleft()

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0 <= ny < N:
                if g[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    
    cnt += 1

    return cnt

for i in range(M):
    for j in range(N):
        if g[i][j] == 1 and not visited[i][j]:
            ans = bfs(i, j)

print(ans)