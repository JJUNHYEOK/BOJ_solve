import sys

input = sys.stdin.readline

k = int(input())
arr = list(map(int,input().split()))
tree = [[] for _ in range(k)]

def deploy(start, end, k):
    if start > end:
        return None
    mid = (start+end)//2
    tree[k].append(arr[mid])
    deploy(start, mid-1, k+1)
    deploy(mid+1, end, k+1)

deploy(0, len(arr)-1, 0)

for val in tree:
    print(*val)