# Question: Grid Index
# Categories: 7 Kyu

def grid_index(grid: list[list[int]], indexes: list[int]) -> str:
    flattened_grid = []

    for i in range(len(grid)):
        flattened_grid.extend(grid[i])
    
    result = ''

    for i in range(len(indexes)):
        result += flattened_grid[indexes[i] - 1]

    return result