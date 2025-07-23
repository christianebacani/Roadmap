# Question: Bumps in the Road
# Categories: 7 Kyu

def bumps(road: str) -> str:
    total_bumps = 0

    for i in range(len(road)):
        if road[i] == 'n':
            total_bumps += 1
    
    if total_bumps <= 15:
        return 'Woohoo!'
    
    return 'Car Dead'