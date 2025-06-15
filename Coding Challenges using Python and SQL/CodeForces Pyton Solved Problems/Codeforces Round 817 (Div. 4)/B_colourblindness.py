# B - Colourblindness

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    grid = []

    for _ in range(2):
        grid.append(input().strip())
    
    grid_is_identical = True

    for i in range(len(grid[0])):
        if (grid[0][i] == grid[1][i]) or (grid[0][i] in ['G', 'B'] and grid[1][i] in ['G', 'B']):
            continue

        grid_is_identical = False
        break

    if grid_is_identical:
        print('YES')
    
    else:
        print('NO')