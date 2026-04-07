import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

N, M, R = map(int,input().split())
g = [[] for _ in range(N+1)]
visited = [-1]*(N+1)

for _ in range(M):
    u, v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)

    
def dfs(R, depth):
    visited[R] = depth
    g[R].sort()
    
    for i in g[R]:
        if visited[i] == -1:
            dfs(i, depth+1)
    
dfs(R, 0)

for i in range(1, N+1):
    print(visited[i])