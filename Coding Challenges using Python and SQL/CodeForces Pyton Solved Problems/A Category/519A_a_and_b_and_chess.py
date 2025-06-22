# 519A - A and B and Chess

chessboard = []

for _ in range(8):
    chessboard.append(input().strip())

chess_piece_and_weight = {
    'Q': 9,
    'q': 9,
    'R': 5,
    'r': 5,
    'B': 3,
    'b': 3,
    'N': 3,
    'n': 3,
    'P': 1,
    'p': 1
}
white_player_total_weight, black_player_total_weight = 0, 0

for chess_piece, weight in chess_piece_and_weight.items():
    total_weight = 0

    for i in range(len(chessboard)):
        if chess_piece not in chessboard[i]:
            continue

        total_weight += (chessboard[i].count(chess_piece) * weight)
    
    if chess_piece.isupper():
        white_player_total_weight += total_weight
    
    else:
        black_player_total_weight += total_weight

if white_player_total_weight > black_player_total_weight:
    print('White')

elif black_player_total_weight > white_player_total_weight:
    print('Black')

else:
    print('Draw')