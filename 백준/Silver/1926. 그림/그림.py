import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*(m) for _ in range(n)]
mx = 0
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    area = 1
    visited[x][y] = 1

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                area += dfs(nx, ny)

    return area

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            area = dfs(i, j)
            mx = max(mx, area)

print(cnt)
print(mx)