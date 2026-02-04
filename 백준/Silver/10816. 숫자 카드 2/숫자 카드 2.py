import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
mine = list(map(int,input().split()))
mine.sort()

m = int(input())
goal = list(map(int,input().split()))

for num in goal:
    cnt = bisect_right(mine,num) - bisect_left(mine,num)
    print(cnt, end=' ')