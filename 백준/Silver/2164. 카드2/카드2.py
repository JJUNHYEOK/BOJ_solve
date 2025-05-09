from collections import deque

def last_card(N):
    q = deque(range(1, N+1)) 

    while len(q) > 1:
        q.popleft()          
        q.append(q.popleft())  

    return q[0]              

n = int(input())

print(last_card(n))