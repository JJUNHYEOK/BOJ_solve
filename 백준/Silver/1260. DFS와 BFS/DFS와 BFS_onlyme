from collections import deque

n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

dfs_result = []
bfs_result = []

def dfs(start):
    visited_dfs[start] = True
    dfs_result.append(start)

    for nxt in graph[start]:
        if not visited_dfs[nxt]:
            dfs(nxt)
    
def bfs(start):
    q = deque()
    q.append(start)
    visited_bfs[start] = True
    bfs_result.append(start)

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                q.append(nxt)
                bfs_result.append(nxt)

dfs(v)
bfs(v)

print(*dfs_result)
print(*bfs_result)    


