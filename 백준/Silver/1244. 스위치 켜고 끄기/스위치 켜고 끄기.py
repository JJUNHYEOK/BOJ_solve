import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

num = [[0]*(N+1)]

for i in range(1,N+1):
    num[0][i] = i

button = deque(map(int,input().split()))
button.appendleft(0)
button = list(button)
num.append(button)

def switching(a, b):
    mid = 0
    left = 0
    right = 0
    
    if a == 1:
        for i in range(1, N+1):
            if i%b == 0:
                if num[1][i] == 0:
                    num[1][i] = 1
                else:
                    num[1][i] = 0

    if a == 2:
        mid = b
        left = mid - 1
        right = mid + 1

        while left >= 1 and right <= N:
            if num[1][left] != num[1][right]:
                break

            left -= 1
            right += 1

        for j in range(left+1, right):
            if num[1][j] == 0:
                num[1][j] = 1
            else:
                num[1][j] = 0

    return num

students = int(input())

for _ in range(students):
    gender, order = map(int,input().split())
    switching(gender, order)

for i in range(1, N+1):
    print(num[1][i], end=" ")
    if i%20 == 0:
        print()