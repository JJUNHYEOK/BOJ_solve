import sys

input = sys.stdin.readline

A, B, C = map(int,input().split())
g = [[] for _ in range(11)]

for i in range(1, 11):
    for j in range(1, 11):
        if A*i + B*j == C:
            g[i].append(j)
            
for i in range(1, 11):
    if not g[i]:
        print(0)
        
    else:
        if len(g[i]) == 1:
            print(g[i][0])
            
        else:
            for data in g[i]:
                print(data)