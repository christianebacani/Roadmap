# Question: A wolf in sheep's clothing
# Categories: 8 Kyu

def warn_the_sheep(queue: list[str]) -> str:
    queue = queue[::-1]

    if queue[0] == 'wolf':
        return 'Pls go away and stop eating my sheep'
    
    for i in range(len(queue)):
        if queue[i] == 'wolf':
            return f'Oi! Sheep number {i}! You are about to be eaten by a wolf!'