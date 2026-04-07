import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
X, Y = map(int,input().split())

g = [[0]*(N+1) for _ in range(N+1)]
targets = []

for _ in range(M):
    A, B = map(int,input().split())
    targets.append((A,B))


dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

dist = [[-1]*(N+1) for _ in range(N+1)]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for d in range(8):
            nx = x+dx[d]
            ny = y+dy[d]

            if 1 <= nx <= N and 1 <= ny <= N:
                if dist[nx][ny] == -1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1

    return dist

ans = bfs(X,Y)

for i in range(len(targets)):
    a, b = targets[i]
    print(dist[a][b], end=' ')