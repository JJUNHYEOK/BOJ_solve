a, b = map(int,input().split())
c = int(input())

h = a
m = b+c

h += m//60
m %= 60
h %= 24

print(h, m)