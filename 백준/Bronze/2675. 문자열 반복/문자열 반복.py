t = int(input())
c_result = []

for _ in range(t):
  r, s = input().split()
  chars = list(s)
  r = int(r)

  result = ''
  for ch in chars:
    result += ch*r

  c_result.append(result)

for char in c_result:
  print(char)