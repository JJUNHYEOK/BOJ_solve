import sys

input = sys.stdin.readline

n = int(input())
mine = list(map(int,input().split()))
mine.sort()
m = int(input())

def bsearch(arr, start, end, target):
    
    while start <= end:

        mid = (start+end)//2

        if arr[mid] == target:
            return 1

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return 0

goal = list(map(int,input().split()))

for num in goal:
    print(bsearch(mine, 0, len(mine)-1, num), end=' ')