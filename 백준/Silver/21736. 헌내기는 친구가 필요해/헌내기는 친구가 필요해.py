import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int,input().split())

univ = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find(arr):
    x, y = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'I':
                x, y = i, j

    return x,y

def friends(a, b):
    cnt, nx, ny = 0, 0, 0

    if univ[a][b] == 'P':
        cnt += 1

    univ[a][b] = 'X'

    for i in range(4):
            nx, ny = a+dx[i], b+dy[i]

            if 0<=nx<n and 0<=ny<m and univ[nx][ny] != 'X':
                cnt += friends(nx, ny)



    return cnt

f, k = find(univ)
result = friends(f, k)

if result == 0:
    print('TT')
else:
    print(result)
