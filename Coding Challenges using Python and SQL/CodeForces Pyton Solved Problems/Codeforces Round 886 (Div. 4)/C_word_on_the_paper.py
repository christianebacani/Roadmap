# C - Word on the Paper

t = input().strip()

for _ in range(int(t)):
    grid = []

    for _ in range(8):
        grid.append(input().strip())

    for i in range(8):
        written_in_the_column = ''

        for j in range(len(grid)):
            written_in_the_column += grid[j][i]
        
        written_in_the_column = written_in_the_column.replace('.', '')

        if written_in_the_column != '':
            print(written_in_the_column)
            break