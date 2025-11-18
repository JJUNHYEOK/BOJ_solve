import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int,input().split())
    graph[u].append((v,w)) # 양방향이 아니므로 graph[u]만 업데이트

s, e = map(int,input().split())

INF = float("INF") # 파이썬에서 inf 처리 -> 암기하기 !
dis = [INF]*(n+1) # 거리 저장 리스트

def dijkstra(start):
    visited = [False]*(n+1) # 방문처리용
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0

    while q:
        d, v = heapq.heappop(q)
        if visited[v]:
            continue

        visited[v] = True
        for nv, nw in graph[v]:
            distance = d + nw
            if distance < dis[nv]:
                dis[nv] = distance
                heapq.heappush(q, (distance, nv))


dijkstra(s)

print(dis[e])
