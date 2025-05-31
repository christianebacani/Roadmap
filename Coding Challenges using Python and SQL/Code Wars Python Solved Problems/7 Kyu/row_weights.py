# Question: Row Weights
# Categories: 7 Kyu

def row_weights(array: list[int]) -> tuple[int]:
    team_one, team_two = [], []

    for i in range(len(array)):
        if i % 2 == 0:
            team_one.append(array[i])
        
        else:
            team_two.append(array[i])
    
    return tuple([sum(team_one), sum(team_two)])