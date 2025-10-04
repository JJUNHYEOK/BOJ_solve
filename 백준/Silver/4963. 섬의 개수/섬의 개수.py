import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
output = []

def dfs(x, y):
    visited[x][y] = True

    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

while True:
    w,h = map(int,input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int,input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    result = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                result += 1
    
    output.append(result)


for data in output:
    print(data)
