arr = []

for i in range(9):
  n = int(input())
  arr.append(n)


maxValue = max(arr)
maxPos = arr.index(maxValue) + 1

print(maxValue)
print(maxPos)
