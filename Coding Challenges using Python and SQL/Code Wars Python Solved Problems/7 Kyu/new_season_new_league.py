# Question: New season, new league
# Categories: 7 Kyu

def premier_league_standings(teams: dict[int, str]) -> dict[int, str]:
    result = {}
    list_of_teams = []
    
    for rank, team in teams.items():
        if rank == 1:
            result[rank] = team
        
        else:
            list_of_teams.append(team)
    
    list_of_teams = sorted(list_of_teams)

    for i in range(len(list_of_teams)):
        result[max(list(result.keys())) + 1] = list_of_teams[i]

    return result