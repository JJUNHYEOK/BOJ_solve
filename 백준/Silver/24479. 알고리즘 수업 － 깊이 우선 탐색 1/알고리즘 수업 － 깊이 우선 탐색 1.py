import sys

sys.setrecursionlimit(200000)
input = sys.stdin.readline

n, m, r = map(int, input().split())  # vertex, edge, start

graph = [[] for _ in range(n + 1)] # 평소와 동일
visited = [False] * (n + 1) # 평소와 동일 
order = [0] * (n + 1) # vertex i의 방문 순서 번호
cnt = 1 # 현재까지 방문한 vertex 개수

for _ in range(m):
  a, b = map(int, input().split())

  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n + 1):
  graph[i].sort()


def dfs(node):
  global cnt
  visited[node] = True
  order[node] = cnt
  cnt += 1

  for neighbor in graph[node]:
    if not visited[neighbor]:
      dfs(neighbor)

dfs(r)

for i in range(1, n + 1):
  print(order[i])
