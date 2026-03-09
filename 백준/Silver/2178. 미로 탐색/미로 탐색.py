import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

    return graph

bfs(0,0)

print(graph[n-1][m-1])