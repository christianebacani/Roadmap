# 2033A - Sakurako and Kosuke

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    list_of_players_turn = []
    x = 0
    move = 1

    while True:
        if move % 2 != 0:
            x = (move * -1)
            list_of_players_turn.append('Sakurako')

        else:
            x = move
            list_of_players_turn.append('Kosuke')

        move += 1

        if ((n * -1) > x) or (x > n):
            break

    print(list_of_players_turn[-1])