import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dis = [-1]*(n+1)
    cnt = 0
    q = deque()
    q.append(start)
    dis[start] = 0

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if dis[nxt] == -1:
                dis[nxt] = dis[cur] + 1
                q.append(nxt)

    for i in range(2, n+1):
        if 1 <= dis[i] <= 2:
            cnt += 1

    return cnt

print(bfs(1))