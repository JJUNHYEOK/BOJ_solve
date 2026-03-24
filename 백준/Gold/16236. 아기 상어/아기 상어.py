import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
g = [list(map(int,input().split())) for _ in range(N)]
size = 2

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(sx, sy):
    q = deque()
    global size
    fish = []
    q.append((sx, sy))

    visited = [[False]*(N) for _ in range(N)]
    visited[sx][sy] = True
    cnt_map = [[0]*(N) for _ in range(N)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and g[nx][ny] <= size:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt_map[nx][ny] = cnt_map[x][y] + 1

                    if 0 < g[nx][ny] < size:
                        fish.append((cnt_map[nx][ny], nx, ny))
    
    return fish



for i in range(N):
    for j in range(N):
        if g[i][j] == 9:
            sx, sy = i, j
            g[sx][sy] = 0

time = 0
eat = 0

while True:

    fish = bfs(sx, sy)

    if not fish:
        break

    fish.sort()
    dist, nx, ny = fish[0]

    time += dist
    sx, sy = nx, ny

    g[nx][ny] = 0

    eat += 1
    
    if eat == size:
        size += 1
        eat = 0

print(time)