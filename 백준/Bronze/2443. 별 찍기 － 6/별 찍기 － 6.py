import sys

input = sys.stdin.readline

n = int(input())

for i in range(2*n-1, 0, -2):
    spc = ((2*n-1)-i)//2
    print(' '* spc + '*'*i)