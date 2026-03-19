import sys
sys.setrecursionlimit(int(1e9))

input = sys.stdin.readline

T = int(input())

def dfs(idx):
    global cnt
    visited[idx] = True
    nx = graph[idx]
    
    if not visited[nx]:
        dfs(nx)

    else:
        if not finished[nx]:
            cur = nx
            cnt += 1
            
            while cur != idx:
                cur = graph[cur]
                cnt += 1

    finished[idx] = True


for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    graph = [0]*(n+1)

    for i in range(n):
        graph[i+1] = arr[i]

    visited = [False]*(n+1)
    finished = [False]*(n+1)

    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    print(n - cnt)