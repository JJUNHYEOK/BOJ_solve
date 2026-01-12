import sys

input = sys.stdin.readline

n = int(input())

for j in range(1, n+1):
    print('*'*j)

for i in range(n-1,0,-1):
    print('*'*i)