a, b, c = map(int, input().split())
list = [a, b, c]
result = 0

if a == b == c:
  result = 10000 + a * 1000

elif a != b and b != c and a != c:
  result = max(list) * 100

else:
  if a == b or a == c:
    same = a

  else:
    same = b

  result = 1000 + same * 100

print(result)