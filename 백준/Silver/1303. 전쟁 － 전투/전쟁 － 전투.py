import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int,input().split())
g = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def ally(i, j):
    q = deque()
    q.append((i, j))
    g[i][j] = 0
    cnt = 1

    while q:
        ax, ay = q.popleft()

        for d in range(4):
            nax = ax+dx[d]
            nay = ay+dy[d]

            if 0 <= nax < N and 0 <= nay < M:
                if g[nax][nay] == 'W':
                    q.append((nax, nay))
                    g[nax][nay] = 0
                    cnt += 1

    return cnt

def enemy(i, j):
    q = deque()
    q.append((i, j))
    g[i][j] = 0
    cnt = 1

    while q:
        ex, ey = q.popleft()

        for d in range(4):
            nex = ex+dx[d]
            ney = ey+dy[d]

            if 0 <= nex < N and 0 <= ney < M:
                if g[nex][ney] == 'B':
                    q.append((nex, ney))
                    g[nex][ney] = 0
                    cnt += 1
    
    return cnt

cnt_a = 0
ans_a = 0
cnt_b = 0
ans_b = 0

for i in range(N):
    for j in range(M):
        if g[i][j] == 'W':
            cnt_a = ally(i, j)
            ans_a += cnt_a**2

for i in range(N):
    for j in range(M):
        if g[i][j] == 'B':
            cnt_b = enemy(i, j)
            ans_b += cnt_b**2

print(ans_a, ans_b)