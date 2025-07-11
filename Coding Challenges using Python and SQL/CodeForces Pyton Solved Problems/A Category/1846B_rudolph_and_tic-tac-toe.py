# 1846B - Rudolph and Tic-Tac-Toe

t = int(input().strip())

for _ in range(t):
    tic_tac_toe_board = []

    for _ in range(3):
        tic_tac_toe_board.append(input().strip())
    
    possible_horizontal_moves = []
    possible_vertical_moves = []
    possible_diagonal_moves = []

    for i in range(len(tic_tac_toe_board)):
        possible_horizontal_moves.append(tic_tac_toe_board[i])
    
    for i in range(len(tic_tac_toe_board[0])):
        possible_vertical_moves.append(tic_tac_toe_board[0][i] + tic_tac_toe_board[1][i] + tic_tac_toe_board[2][i])
    
    possible_diagonal_moves.append(tic_tac_toe_board[0][0] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][2])
    possible_diagonal_moves.append(tic_tac_toe_board[0][2] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][0])
    
    list_of_possible_moves = []

    for i in range(len(possible_horizontal_moves)):
        list_of_possible_moves.append(possible_horizontal_moves[i])
    
    for i in range(len(possible_vertical_moves)):
        list_of_possible_moves.append(possible_vertical_moves[i])
    
    for i in range(len(possible_diagonal_moves)):
        list_of_possible_moves.append(possible_diagonal_moves[i])
    
    answer = 'DRAW'
    
    for i in range(len(list_of_possible_moves)):
        if len(set(list_of_possible_moves[i])) != 1:
            continue

        if list_of_possible_moves[i][0] == '.':
            continue

        answer = list_of_possible_moves[i][0]
        break

    print(answer)