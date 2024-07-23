n = int(input())

numbers = list(map(int,input().split()))

maximum = numbers[0]
minimum = numbers[0]

for i in range(len(numbers)):
  if numbers[i] > maximum:
    maximum = numbers[i]
  if numbers[i] < minimum:
    minimum = numbers[i]

print(minimum, end = ' ')
print(maximum)
