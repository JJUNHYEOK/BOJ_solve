import sys
from collections import deque

n = int(input())
k = int(input())
g = [[0]*n for _ in range(n)]

for _ in range(k):
    sx, sy = map(int,input().split())
    g[sx-1][sy-1] = 2

l = int(input())

dir = {}

for _ in range(l):
    x, c = input().split()
    dir[int(x)] = c

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0
xx, yy = 0, 0
g[xx][yy] = 1
d = 0
q = deque()
q.append((xx, yy))

while True:
    time += 1
    nx, ny = xx+dx[d], yy+dy[d]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= n or g[nx][ny] == 1:
        break

    else:
        if g[nx][ny] == 2:
            g[nx][ny] = 1
            q.append((nx, ny))

        else:
            g[nx][ny] = 1
            q.append((nx, ny))
            ox, oy = q.popleft()
            g[ox][oy] = 0

    if time in dir: # KeyError 방지용
                if dir[time] == 'L':
                    d = (d+3)%4

                else:
                    d = (d+1)%4
    
    xx, yy = nx, ny

print(time)