import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]

dx = [0, 1]
dy = [1, 0]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    graph[sx][sy] = -1

    while q:

        x, y = q.popleft()

        if x == m-1 and y == n-1:
            return True

        for i in range(2):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = -1

    return False

if bfs(0,0) == True:
    print('Yes')

else:
    print('No')