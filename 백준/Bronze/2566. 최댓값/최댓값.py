table = []
row, col = 0, 0
val = -1

for _ in range(9):
    table.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):

        if table[i][j] > val:
            val = table[i][j]
            row, col = i+1, j+1



       

print(val)
print(row, col)