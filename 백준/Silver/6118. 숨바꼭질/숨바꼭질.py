import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
g = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(N+1):
    g[i].sort()

def bfs(start):
    cnt_map = [0]*(N+1)
    visited = [False]*(N+1)
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()

        for nxt in g[cur]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                cnt_map[nxt] = cnt_map[cur] + 1

    return cnt_map

result = bfs(1)
idx = 0
num = 0
ans = max(result)


for i in range(1, N+1):
    if result[i] == ans:
        num += 1
        if idx == 0:
            idx = i

print(idx, ans, num)