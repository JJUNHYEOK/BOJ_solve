import sys
input = sys.stdin.readline

n = int(input())
room = set()

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        room.add(name)
    else:
        room.remove(name)

for name in sorted(room, reverse=True):
    print(name)
