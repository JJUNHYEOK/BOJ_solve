import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
g = [[0]*N for _ in range(N)]
dist = [[0]*N for _ in range(N)]

r1, c1, r2, c2 = map(int,input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    g[sx][sy] = 1

    while q:
        x, y = q.popleft()

        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and  0 <= ny < N:
                if g[nx][ny] == 0:
                    q.append((nx, ny))
                    g[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1

    return dist

ans = bfs(r1, c1)

if ans[r2][c2] == 0:
    print(-1)

else:
    print(ans[r2][c2])