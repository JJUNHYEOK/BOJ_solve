n = int(input())
numbers = []

for _ in range(n):
  num = int(input())
  numbers.append(num)

sorted_numbers = sorted(numbers)

for i in range(n):
  print(sorted_numbers[i])

