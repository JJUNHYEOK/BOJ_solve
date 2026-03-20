import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int,input().split())
g = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fire_time = [[-1]*C for _ in range(R)]

def fire():
    q = deque()

    for i in range(R):
        for j in range(C):
            if g[i][j] == 'F':
                q.append((i, j))
                fire_time[i][j] = 0

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C: # 범위 체크가 항상 1번
                continue
            if g[nx][ny] == '#':
                continue
            if fire_time[nx][ny] != -1:
                continue

            fire_time[nx][ny] = fire_time[x][y] + 1
            q.append((nx, ny))

def bfs():
    q = deque()
    dis = [[-1]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if g[i][j] == 'J':
                q.append((i, j))
                dis[i][j] = 0

    while q:

        x, y = q.popleft()

        if x == 0 or x == R-1 or y == 0 or y == C-1: # 탈출 조건 !!!@#@!#
            return dis[x][y] + 1

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if g[nx][ny] == '#':
                continue
            if dis[nx][ny] != -1:
                continue
            if fire_time[nx][ny] != -1 and fire_time[nx][ny] <= dis[x][y] + 1:
                continue

            dis[nx][ny] = dis[x][y] + 1
            q.append((nx, ny))

    return "IMPOSSIBLE"

fire()
print(bfs())