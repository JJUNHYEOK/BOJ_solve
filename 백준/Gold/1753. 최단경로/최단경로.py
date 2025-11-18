import heapq
import sys

input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())

INF = float("INF")
arr = [[]*(V+1) for _ in range(V+1)]
dis = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int,input().split())
    arr[u].append((v,w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0

    while q:
        d, v = heapq.heappop(q)
        if dis[v] < d:
            continue

        for nv, nw in arr[v]:
            distance = d+nw
            if distance < dis[nv]:
                dis[nv] = distance
                heapq.heappush(q, (distance, nv))


dijkstra(K)


for d in dis[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)