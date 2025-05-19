# Question: Rock Paper Scissors!
# Categories: 8 Kyu

def rps(player1_move, player2_move) -> str:
    winning_move = {
        'scissors': 'paper',
        'paper': 'rock',
        'rock': 'scissors'
    }

    if winning_move[player1_move] == player2_move:
        return 'Player 1 won!'
    
    elif winning_move[player2_move] == player1_move:
        return 'Player 2 won!'
    
    else:
        return 'Draw!'