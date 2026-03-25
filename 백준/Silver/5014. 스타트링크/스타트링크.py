import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int,input().split())
g =[0]*(F+1)
visited = [False]*(F+1)

def bfs(floor):
    q = deque()
    q.append(floor)
    visited[floor] = True

    while q:
        cur = q.popleft()

        if cur == G:
            return g[cur]

        up = cur + U
        down = cur - D

        if 0 < up <= F and not visited[up]:
            visited[up] = True
            g[up] = g[cur] + 1
            q.append(up)

        if 0 < down <= F and not visited[down]:
            visited[down] = True
            g[down] = g[cur] + 1
            q.append(down)

    return 'use the stairs'

print(bfs(S))