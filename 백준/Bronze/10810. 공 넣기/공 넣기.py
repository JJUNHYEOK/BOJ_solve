n,m = map(int,input().split())

arr = [0]*n

for row in range(m):
  i,j,k = map(int,input().split())

  for p in range(i,j+1):
    arr[p-1] = k

for i in range(n):
  print(arr[i], end=' ')


