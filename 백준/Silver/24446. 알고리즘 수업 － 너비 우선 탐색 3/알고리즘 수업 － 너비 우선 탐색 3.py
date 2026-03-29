import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int,input().split())
g = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(start):
    q = deque()
    visited = [False]*(N+1)
    cnt_map = [0]*(N+1)
    q.append(start)
    visited[start] = True
    cnt_map[start] = 0

    while q:
        cur = q.popleft()

        for nxt in g[cur]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                cnt_map[nxt] = cnt_map[cur] + 1

    
    return cnt_map

result = bfs(R)

for i in range(1, N+1):
    if i != R and result[i] == 0:
        print(-1)

    else:
        print(result[i])