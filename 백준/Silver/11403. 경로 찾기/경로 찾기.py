import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
result = [[0]*n for _ in range(n)]

def bfs(start):
    q = deque([start])
    visited = [False]*n

    while q:
        cur = q.popleft()
        for nxt in range(n):
            if graph[cur][nxt] == 1 and not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return visited


ans = []

for i in range(n):
    possible = bfs(i)
    for j in range(n):
        result[i][j] = 1 if possible[j] else 0

for row in result:
    print(*row)
