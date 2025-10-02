import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()
result = []

for _ in range(n):
    cmd = input().split() 
    a = cmd[0] # split으로 받은 문자열을 배열처럼 인덱스로 쪼갤 수 있다 !
    if len(cmd) > 1 :
        b = cmd[1]

    if a == '1':
        q.appendleft(b)

    elif a == '2':
        q.append(b)

    elif a == '3':
        if q:
            result.append(q.popleft())
        
        else:
            result.append(-1)

    elif a == '4':
        if q:
            result.append(q.pop())
        
        else:
            result.append(-1)

    elif a == '5':
        result.append(len(q))

    elif a == '6':
        if q:
            result.append(0)

        else:
            result.append(1)

    elif a == '7':
        if q:
            result.append(q[0])

        else:
            result.append(-1)

    elif a == '8':
        if q:
            result.append(q[-1])
        else:
            result.append(-1)


for num in result:
    print(num)