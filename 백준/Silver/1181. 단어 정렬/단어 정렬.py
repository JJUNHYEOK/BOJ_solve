import sys

input = sys.stdin.readline

n = int(input())
lyrics = []

for _ in range(n):
    lyrics.append(input().strip())

lyrics = list(set(lyrics))

lyrics.sort(key = lambda x: (len(x), x))

for l in lyrics:
    print(l)