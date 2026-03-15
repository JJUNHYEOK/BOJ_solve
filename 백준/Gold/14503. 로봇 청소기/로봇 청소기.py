import sys

input = sys.stdin.readline

n, m = map(int,input().split())
r, c, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

while True:

    if graph[r][c] == 0:
        graph[r][c] = 2
        cnt += 1

    moved = False

    for _ in range(4):

        d = (d+3)%4
        nx = r+dx[d]
        ny = c+dy[d]

        if graph[nx][ny] == 0:
            r, c = nx, ny
            moved = True
            break

    if not moved:

        back = (d+2)%4
        nx = r+dx[back]
        ny = c+dy[back]

        if graph[nx][ny] == 1:
            break
        else:
            r, c = nx, ny

print(cnt)