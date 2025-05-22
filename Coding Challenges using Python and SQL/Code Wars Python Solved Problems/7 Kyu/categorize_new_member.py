# Question: Categorize New Member
# Categories: 7 Kyu

def open_or_senior(data_of_potential_members: list[list[int]]) -> list[str]:
    result = []

    for i in range(len(data_of_potential_members)):
        age = data_of_potential_members[i][0]
        handicap = data_of_potential_members[i][1]

        if age > 54 and handicap > 7:
            result.append('Senior')
        
        else:
            result.append('Open')
    
    return result