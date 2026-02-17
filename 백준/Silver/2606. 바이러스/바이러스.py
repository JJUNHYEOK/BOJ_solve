import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

def dfs(start):
    global cnt
    visited[start] = True

    for cur in graph[start]:
        if not visited[cur]:
            cnt += 1
            dfs(cur)

dfs(1)
print(cnt)