import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    word = input().strip()
    print(word[0] + word[-1])
