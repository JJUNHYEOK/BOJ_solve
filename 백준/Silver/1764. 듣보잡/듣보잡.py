import sys

input = sys.stdin.readline

n, m = map(int,input().split())

unseen = set()
unheard = set()

for _ in range(n):
    name = input().rstrip()
    unseen.add(name)

for _ in range(m):
    name = input().rstrip()
    unheard.add(name)

result = sorted(unseen&unheard)

print(len(result))

for name in result:
    print(name)