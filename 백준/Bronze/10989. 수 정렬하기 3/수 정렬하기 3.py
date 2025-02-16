import sys

def inputs():
  return sys.stdin.readline()

n = int(inputs())

count = [0]*10001

for _ in range(n):
  num = int(inputs())
  count[num] += 1

for i in range(1,10001):
  if count[i] != 0:
    for _ in range(count[i]):
      print(i)



