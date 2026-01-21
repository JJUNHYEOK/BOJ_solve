import sys

input = sys.stdin.readline

n = int(input())
origami = [[0]*100 for _ in range(100)]

def colored(a, b):
    for i in range(a, a+10):
        for j in range(b, b+10):
            origami[i][j] = 1

    return origami

def area(arr):
    cnt = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:
                cnt +=1

    return cnt


for _ in range(n):
    x, y = map(int,input().split())
    colored(x,y)

print(area(origami))
