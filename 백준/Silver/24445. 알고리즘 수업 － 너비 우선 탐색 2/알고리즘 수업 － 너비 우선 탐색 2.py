import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort(reverse=True)

def bfs(start):
    visited = [0]*(n+1)
    
    cnt = 1
    visited[start] = cnt
    
    q = deque()
    q.append(start)

    while q:
        d = q.popleft()
        for nxt in graph[d]:
            if visited[nxt] == 0:
                cnt += 1
                visited[nxt] = cnt
                q.append(nxt)
            
    for i in range(1, n+1):
        print(visited[i])



bfs(r)
