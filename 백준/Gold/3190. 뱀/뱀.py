import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[0]*n for _ in range(n)]
time = 0
sr, sc = 0, 0 # 초기 출발 위치는 fix
graph[sr][sc] = -1 # 뱀이 처음 출발하는 곳, 길어지면 다른 곳들도 -1로 전파됨.

k = int(input())

for _ in range(k):
    r, c = map(int,input().split())
    graph[r-1][c-1] = 2 # 사과 있는 곳은 2로 표현

l = int(input())

direction = {}

for _ in range(l):
    x, ch = input().split()
    direction[int(x)] = ch

d = 0 # 오른쪽 방향 벡터
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque()
snake.append((sr, sc))

while True:
    
    time += 1

    nx = sr + dx[d]
    ny = sc + dy[d]

    # 벽 충돌 ㅋㅋ
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break

    # 몸빵
    if graph[nx][ny] == -1:
        break

    # 이동해라 ~
    snake.append((nx, ny))

    # 사과 처리
    if graph[nx][ny] == 2:
        graph[nx][ny] = -1
    
    else:
        tx, ty = snake.popleft()
        graph[tx][ty] = 0

    graph[nx][ny] = -1
    sr, sc = nx, ny

    # 방향 바꿔야지
    if time in direction:

        if direction[time] == 'L':
            d = (d+3)%4
        else:
            d = (d+1)%4

print(time)