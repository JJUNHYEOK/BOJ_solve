n, k = map(int, input().split())
scores = []
numbers = list(map(int, input().split()))

numbers.sort()

for i in reversed(range(n)):
  reversed_numbers = numbers[i]
  scores.append(reversed_numbers)


print(scores[k-1])


