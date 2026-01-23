import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    floor = int(input())
    room = int(input())
    
    mem = [i for i in range(1, room+1)]

    for _ in range(floor):
        for j in range(1,room):
            mem[j] += mem[j-1]

    print(mem[-1])

