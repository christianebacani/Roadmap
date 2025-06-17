# 1535A - Fair Playoff

t = int(input().strip())

for _ in range(t):
    skills_of_each_players = input().strip().split()
    skills_of_each_players = [int(skill) for skill in skills_of_each_players]
    
    first_match = skills_of_each_players[:2]
    second_match = skills_of_each_players[2:]

    winner_of_first_match = max(first_match)
    winner_of_second_match = max(second_match)
    
    sorted_skills_of_each_players = sorted(skills_of_each_players, reverse=True)
    first_highest_skill = sorted_skills_of_each_players[0]
    second_highest_skill = sorted_skills_of_each_players[1]

    if first_highest_skill in [winner_of_first_match, winner_of_second_match] and second_highest_skill in [winner_of_first_match, winner_of_second_match]:
        print('YES')

    else:
        print('NO')