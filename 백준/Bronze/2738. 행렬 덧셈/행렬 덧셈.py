n, m = map(int,input().split())

m1 = []
m2 = []


for _ in range(n):
  row = list(map(int,input().split()))
  m1.append(row)

for _ in range(n):
  row = list(map(int,input().split()))
  m2.append(row)

result = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

for i in range(n):
  for j in range(m):
    print(result[i][j], end=' ')
  print()