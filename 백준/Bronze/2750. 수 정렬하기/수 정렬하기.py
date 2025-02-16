def sorting(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(n-1-i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

  return arr

n = int(input())
numbers = []

for _ in range(n):
  num = int(input())
  numbers.append(num)

sorting(numbers)

for i in range(n):
  print(numbers[i])

