import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
t = int(input())


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    visited[y][x] = True
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0<= nx < m and 0 <= ny < n:
            if graph[ny][nx] and not visited[ny][nx]:
                dfs(nx, ny)

for _ in range(t):
    m,n,k = map(int,input().split())
    graph = [[False]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = True
    
    result = 0


    for y in range(n):
        for x in range(m):
            if graph[y][x] and not visited[y][x]:
                dfs(x,y)
                result += 1


    print(result)


