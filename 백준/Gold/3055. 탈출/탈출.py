import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int,input().split())
graph = [list(map(str,input().rstrip())) for _ in range(r)]
qw = deque()
qs = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            sx, sy = i, j
            qs.append((i, j))
        if graph[i][j] == '*':
            qw.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    time = 0
    visited = [[False]*c for _ in range(r)]
    visited[sx][sy] = True

    while qs:

        for _ in range(len(qw)):
            x, y = qw.popleft()

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]

                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = '*'
                        qw.append((nx, ny))


        for _ in range(len(qs)):
            x, y = qs.popleft()

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]

                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == 'D':
                        return time+1
                    
                    if graph[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        qs.append((nx, ny))

        time += 1

    return "KAKTUS"

print(bfs())