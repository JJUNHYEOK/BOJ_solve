n = list(map(int,input()))
result = []
listed_num = sorted(n)

for i in reversed(range(len(listed_num))):
  result.append(listed_num[i])

for i in range(len(result)):
  print(result[i], end = '')

