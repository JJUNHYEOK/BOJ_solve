import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
result = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    global visited, result
    visited[v] = True

    for i in range(1, n+1):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i)
        
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)
