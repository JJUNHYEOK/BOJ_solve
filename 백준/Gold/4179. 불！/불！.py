import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int,input().split())
g = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fire_time = [[-1]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if g[i][j] == 'J':
            si, sj = i, j

def bfs():
    q = deque()
    dist = [[-1]*C for _ in range(R)]
    q.append((si, sj))
    dist[si][sj] = 0

    while q:

        x, y = q.popleft()

        if x == 0 or x == R-1 or y == 0 or y == C-1:
            return dist[x][y] + 1

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if g[nx][ny] == '#':
                continue
            if dist[nx][ny] != -1:
                continue

            if fire_time[nx][ny] != -1 and fire_time[nx][ny] <= dist[x][y] + 1:
                continue

            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
    
    return "IMPOSSIBLE"

def fire():
    q = deque()

    for i in range(R):
        for j in range(C):
            if g[i][j] == 'F':
                q.append((i, j))
                fire_time[i][j] = 0

    while q:
        x, y  = q.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C or g[nx][ny] == '#':
                continue

            if fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[x][y] + 1
                q.append((nx,ny))

fire()
print(bfs())