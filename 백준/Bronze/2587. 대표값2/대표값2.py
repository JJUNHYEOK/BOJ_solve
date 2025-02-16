numbers = []
mid = 2

for i in range(5):
  n = int(input())
  numbers.append(n)

def avg(numbers):
  sum = 0
  for i in range(0,5):
    sum += numbers[i]

  return sum//5

sorted_numbers = sorted(numbers)
mid_num = sorted_numbers[mid]

print(avg(numbers))
print(mid_num)

