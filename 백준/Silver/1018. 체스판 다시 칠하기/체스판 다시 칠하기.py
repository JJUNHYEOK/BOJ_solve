import sys

input = sys.stdin.readline

n, m = map(int,input().split())
color = [list(input().rstrip()) for _ in range(n)]

def paint(x, y):
    cntw = 0
    cntb = 0

    for i in range(8):
        for j in range(8):

            if (i+j)%2 == 0:
                if color[x+i][y+j] != 'W':
                    cntw += 1
                if color[x+i][y+j] != 'B':
                    cntb += 1

            else:
                if color[x+i][y+j] != 'B':
                    cntw += 1
                if color[x+i][y+j] != 'W':
                    cntb += 1
    
    return min(cntw, cntb)

ans = 64

for i in range(n-7):
    for j in range(m-7):
        ans = min(ans, paint(i,j))

print(ans)