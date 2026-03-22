import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int,input().split())
g = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, team):
    q = deque()
    q.append((i, j))
    g[i][j] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if g[nx][ny] == team:
                    q.append((nx, ny))
                    g[nx][ny] = 0
                    cnt += 1

    return cnt

ans_w, ans_b = 0, 0

for i in range(N):
    for j in range(M):
        if g[i][j] == 'W':
            cnt = bfs(i, j, 'W')
            ans_w += cnt**2
        elif g[i][j] == 'B':
            cnt = bfs(i, j, 'B')
            ans_b += cnt**2

print(ans_w, ans_b)