import sys

input = sys.stdin.readline

n = int(input())

people = list(map(int,input().split()))
k = len(people)
mem = [0]*k

people.sort()
mem[0] = people[0]

for i in range(1,n):
        mem[i] = mem[i-1] + people[i]

print(sum(mem))