import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))
num.sort()

def bsearch(arr, target, start, end):
    
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return False

m = int(input())

targets = list(map(int,input().split()))

for target in targets:
    result = bsearch(num, target, 0, n-1)

    if result is not False:
        print(1)
    else: print(0)