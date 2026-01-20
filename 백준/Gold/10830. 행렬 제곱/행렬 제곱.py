import sys

input = sys.stdin.readline

n, b = map(int,input().split())

mtrx = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        mtrx[i][j] %= 1000

result = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            result[i][j] = 1

def mtrx_mul(a, b):
    n = len(a)
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += (a[i][k] * b[k][j])%1000
                c[i][j] %= 1000

    return c

while b > 0:
    if b%2 == 1:
        result = mtrx_mul(result, mtrx)
    mtrx = mtrx_mul(mtrx, mtrx)
    b //= 2

for data in result:
    print(*data)