import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dis = [-1]*(n+1)


for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)

def path(start):
    q = deque()
    dis[start] = 0
    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                dis[nxt] = dis[cur] + 1
                q.append(nxt)

path(x)

ans = []

for i in range(1, n+1):
    if dis[i] == k:
        ans.append(i)

if not ans:
    print(-1)
else:
    for num in ans:
        print(num)