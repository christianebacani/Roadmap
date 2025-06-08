# 96A - Football

players_positions = input().strip()
players_positions_is_dangerous = False

for i in range(1, len(players_positions) + 1):
    for j in range(len(players_positions)):
        substring = players_positions[j : j + i]

        if len(substring) != i:
            continue

        if len(set(substring)) != 1:
            continue

        if len(substring) >= 7:
            players_positions_is_dangerous = True
            break

if players_positions_is_dangerous:
    print('YES')

else:
    print('NO')