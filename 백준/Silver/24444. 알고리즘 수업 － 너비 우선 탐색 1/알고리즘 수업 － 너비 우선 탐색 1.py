import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int,input().split())
visited = [False]*(n+1)
order = [0]*(n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, n+1):
    graph[i].sort()


def bfs(start):
    q = deque()
    visited[start] = True
    q.append(start)
    cnt = 1
    order[start] = cnt

    while q:
        v = q.popleft()
        for next in graph[v]:
            if not visited[next]:
                visited[next] = True
                cnt += 1
                order[next] = cnt
                q.append(next)


bfs(r)

for num in range(1, n+1):
    print(order[num])
