n, m = map(int,input().split())
graph = []

for _ in range(m):
    a, b, c = map(int,input().split())
    graph.append((a,b,c))

INF = float("INF")

def bf(start):
    dis = [INF]*(n+1)
    dis[start] = 0

    for i in range(1, n+1):
        for s,e,d in graph:
            if dis[s] == INF:
                continue
            next_dis = dis[s] + d
            if next_dis < dis[e]:
                dis[e] = next_dis
                if i == n:
                    print(-1)
                    return
                
    for d in dis[2:]:
        print(d if d != INF else -1)

bf(1)

