# B - Matrix Rotation

def is_matrix_beautiful(grid: list[list[int]]) -> bool:
    if grid[0][0] > grid[1][0] or grid[0][0] > grid[0][1]:
        return False
    
    elif grid[0][1] > grid[1][1]:
        return False
    
    elif grid[1][0] > grid[1][1]:
        return False
    
    elif grid[1][1] < grid[0][1]:
        return False
    
    else:
        return True

t = int(input().strip())

for _ in range(t):
    matrix = []

    for _ in range(2):
        row = input().strip().split()
        matrix.append([int(r) for r in row])
    
    matrix_is_beautiful = False

    for _ in range(4):
        if is_matrix_beautiful(matrix):
            matrix_is_beautiful = True
            break
        
        # Rotate matrix in 90 degrees
        top_left_element = matrix[0][0]
        top_right_element = matrix[0][1]
        bottom_left_element = matrix[1][0]
        bottom_right_element = matrix[1][1]

        matrix = [
            [bottom_left_element, top_left_element],
            [bottom_right_element, top_right_element]
        ]
    
    if matrix_is_beautiful:
        print('YES')
    
    else:
        print('NO')