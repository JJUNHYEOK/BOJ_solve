import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())

q = deque()
stk = []

for i in range(1, n+1):
    q.append(i)

while q:
    for _ in range(k-1):  
        q.append(q.popleft())

    stk.append(q.popleft())  


print('<'+', '.join(map(str, stk))+'>')