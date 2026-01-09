import sys

input = sys.stdin.readline

n, m = map(int,input().split())
pokemon = {}

for i in range(1,n+1):
    name = input().rstrip()
    pokemon[i] = name
    pokemon[name] = i

for i in range(m):
    cmd = input().rstrip()
    if cmd.isdigit():
        print(pokemon[int(cmd)])
    else:
        print(pokemon[cmd])