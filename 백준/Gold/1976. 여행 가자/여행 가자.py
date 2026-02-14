import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
arr = list(map(int,input().split()))
visited = [False]*(n+1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cur = q.pop()
        for i in range(n):
            if graph[cur][i] and not visited[i]:
                visited[i] = True
                q.append(i)


result = 'YES'
bfs(arr[0]-1)

for a in arr:
    if not visited[a-1]:
        result = 'NO'
        break

print(result)