import sys

input = sys.stdin.readline

result = []

a, b = map(int,input().split())
c, d = map(int,input().split())

# case 1
val = (a/c) + (b/d)
result.append(val)

# case 2
val = (c/d) + (a/b)
result.append(val)

# case 3
val = (d/b) + (c/a)
result.append(val)

# case 4
val = (b/a) + (d/c)
result.append(val)

# Searching
print(result.index(max(result)))