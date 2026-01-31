import sys

input = sys.stdin.readline

arr = [list(input().rstrip()) for _ in range(5)]
# for i in range(5):
#     for j in range(len(arr[i])):
        
#         print(arr[j][i], end='')

for j in range(15):
    for i in range(5):
        if j < len(arr[i]):
            print(arr[i][j], end='')