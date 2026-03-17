import sys

input = sys.stdin.readline

n, m = map(int,input().split())
r, c, d = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(n)]
cnt = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:

    if g[r][c] == 0:
        g[r][c] = 2
        cnt += 1

    moved = False

    for _ in range(4):
        d = (d+3)%4
        nx = r + dx[d]
        ny = c + dy[d]

        if g[nx][ny] == 0:
            r, c = nx, ny
            moved = True
            break
        
    if not moved:

        back = (d+2)%4
        r += dx[back]
        c += dy[back]

        if g[r][c] == 1:
            break

print(cnt)