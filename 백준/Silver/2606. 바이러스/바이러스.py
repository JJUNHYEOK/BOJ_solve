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
    visited[start] = True
    global cnt

    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(nxt)
            cnt += 1

    return cnt

print(dfs(1))
