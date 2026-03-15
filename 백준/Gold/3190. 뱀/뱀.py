import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[0]*n for _ in range(n)]

k = int(input())

for _ in range(k):
    r, c = map(int,input().split())
    graph[r-1][c-1] = 2

l = int(input())
dir = {}

for _ in range(l):
    x, ch = input().split()
    dir[int(x)] = ch

time = 0
sr, sc = 0, 0
graph[sr][sc] = -1
snake = deque()
snake.append((sr, sc))

d = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    time += 1

    nx = sr + dx[d]
    ny = sc + dy[d]

    # 벽 충돌
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break

    # 자기 몸 만났을 때 ㅠ ㅠ
    if graph[nx][ny] == -1:
        break

    # 이동해보자
    snake.append((nx, ny))

    # 사과 처리
    if graph[nx][ny] == 2:
        graph[nx][ny] = -1

    else:
        tx, ty = snake.popleft()
        graph[tx][ty] = 0

    graph[nx][ny] = -1
    sr, sc = nx, ny

    # 방향 전환

    if time in dir:

        if dir[time] == 'L':
            d = (d+3)%4

        else:
            d = (d+1)%4

print(time)