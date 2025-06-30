# 1692C - Where's the Bishop?

t = int(input().strip())

for _ in range(t):
    input()
    chessboard = []

    for _ in range(8):
        chessboard.append(input().strip())
    
    row_position, column_position = 0, 0

    for i in range(len(chessboard)):
        if i == 0 or i == len(chessboard) - 1:
            continue
        
        the_bishop_was_located = False

        for j in range(len(chessboard[i])):
            if j == 0 or j == len(chessboard[i]) - 1:
                continue

            if chessboard[i][j] == '.':
                continue

            if (chessboard[i - 1][j - 1] == '.') or (chessboard[i - 1][j + 1] == '.'):
                continue

            if (chessboard[i + 1][j - 1] == '.') or (chessboard[i + 1][j + 1] == '.'):
                continue

            the_bishop_was_located = True
            column_position = j + 1
            break
        
        if the_bishop_was_located:
            row_position = i + 1
            break
    
    print(f'{row_position} {column_position}')