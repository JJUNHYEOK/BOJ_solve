import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(visited[i])