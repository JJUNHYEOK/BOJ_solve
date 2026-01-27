import sys

input = sys.stdin.readline

n = int(input())
locate = []

for _ in range(n):
    a, b = map(int,input().split())
    locate.append((a,b))

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = (start + end) // 2
    arr[start], arr[pivot] = arr[pivot], arr[start]
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]

        else:
            arr[left], arr[right] = arr[right], arr[left]

    
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

    return arr

quick_sort(locate, 0, len(locate)-1)

for x, y in locate:
    print(x,y)