n = int(input())
number = []

for _ in range(n):
    num = list(map(int,(input().split())))
    number.append(num)

number.sort()


for x,y in number:
  print(x,y)

