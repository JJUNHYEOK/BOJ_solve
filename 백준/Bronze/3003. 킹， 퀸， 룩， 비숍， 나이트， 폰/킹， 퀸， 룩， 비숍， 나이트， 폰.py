import sys

input = sys.stdin.readline

king = 1
queen = 1
look = 2
bishop = 2
knight = 2
pawn = 8

a, b, c, d, e, f = map(int,input().split())

print(king-a, queen-b, look-c, bishop-d, knight-e, pawn-f)