import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deck = deque(range(1, n+1))
drop = []
cnt = 0

while len(deck) > 1:
    drop.append(deck.popleft())
    deck.append(deck.popleft())


for i in range(len(drop)):
    print(drop[i], end = ' ')

print(deck[0])

        
