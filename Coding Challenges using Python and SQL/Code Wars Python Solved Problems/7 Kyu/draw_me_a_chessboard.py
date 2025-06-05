# Question: draw me a chessboard
# Categories: 7 Kyu

def chess_board(rows: int, columns: int) -> list[list[str]]:
    chessboard = []

    for _ in range(rows):
        chessboard.append([])
    
    for i in range(len(chessboard)):
        if i % 2 == 0:
            for j in range(columns):
                if j % 2 == 0:
                    chessboard[i].append('O')
                
                else:
                    chessboard[i].append('X')

        else:
            for j in range(columns):
                if j % 2 != 0:
                    chessboard[i].append('O')
                
                else:
                    chessboard[i].append('X')
    
    return chessboard