import sys 
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
visited_rg = [[False]*n for _ in range(n)]
result = 0
result_rg = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, color):
    
    visited[x][y] = True

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and (not visited[nx][ny] and graph[nx][ny] == color):
                dfs(nx, ny, color)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            result += 1


def dfs_rg(x, y, color):

    visited_rg[x][y] = True

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited_rg[nx][ny]:
            if color == 'B':
                if graph[nx][ny] == 'B':
                    dfs_rg(nx, ny, color)
            
            else:
                if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                    dfs_rg(nx, ny, color)


for i in range(n):
    for j in range(n):
        if not visited_rg[i][j]:
            dfs_rg(i, j, graph[i][j])
            result_rg += 1



print(result, end=' ')
print(result_rg)
