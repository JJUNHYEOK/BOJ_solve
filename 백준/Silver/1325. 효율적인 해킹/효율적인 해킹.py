import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
g = [[] for _ in range(N+1)]
visited = [0]*(N+1)
vid = 1

for _ in range(M):
    a, b = map(int,input().split())
    g[b].append(a)

def bfs(num):
    q = deque()
    q.append(num)
    visited[num] = vid
    cnt = 0

    while q:

        cur = q.popleft()

        for nxt in g[cur]:
            if visited[nxt] != vid:
                visited[nxt] = vid
                q.append(nxt)
                cnt += 1

    return cnt

result = [0]*(N+1)

for i in range(1, N+1):
    result[i] = bfs(i)
    vid += 1

max_cnt = max(result)

for i in range(1, N+1):
    if result[i] == max_cnt:
        print(i, end=' ')  