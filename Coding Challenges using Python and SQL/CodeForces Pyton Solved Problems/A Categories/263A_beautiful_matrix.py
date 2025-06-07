# 263A - Beautiful Matrix

matrix = []

for _ in range(5):
    row = input().split()

    for i in range(len(row)):
        row[i] = int(row[i])
    
    matrix.append(row)

row_where_1_is_located = 0
column_where_1_is_located = 0

for i in range(len(matrix)):
    if 1 not in matrix[i]:
        continue

    row_where_1_is_located = i
    
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            column_where_1_is_located = j

print(abs(row_where_1_is_located - 2) + abs(column_where_1_is_located - 2))