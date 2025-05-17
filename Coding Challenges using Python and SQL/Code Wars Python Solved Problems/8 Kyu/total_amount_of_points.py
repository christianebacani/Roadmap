# Question: Total amount of points
# Categories: 8 Kyu

def points(games: list[str]) -> int:
    total_points = 0

    for i in range(len(games)):
        team_score = int(games[i][0])
        opponent_score = int(games[i][2])

        if team_score > opponent_score:
            total_points += 3

        elif team_score == opponent_score:
            total_points += 1

    return total_points