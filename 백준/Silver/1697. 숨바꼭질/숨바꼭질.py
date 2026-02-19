import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())
visited = [False]*100001

q = deque()

q.append((n, 0))
visited[n] = True

while q:
    x, time = q.popleft()

    if x == k:
        print(time)
        break

    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True
            q.append((nx, time+1))