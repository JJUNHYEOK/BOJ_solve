import sys
sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

a, b = map(int,input().split())
m = int(input())

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = -1

def dfs(start, depth):
    global ans
    visited[start] = True

    if start == b:
        ans = depth
        return

    for cur in graph[start]:
        if not visited[cur]:
            dfs(cur, depth+1)

dfs(a, 0)
print(ans)