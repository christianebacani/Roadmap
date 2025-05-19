# Question: The Office I - Outed
# Categories: 7 Kyu

def outed(name_and_happiness_rating: dict[str, int], boss: str) -> str:
    total_score = 0

    for name, happiness_rating in name_and_happiness_rating.items():
        if name == boss:
            total_score += (happiness_rating * 2)

        else:
            total_score += happiness_rating

    if total_score / len(list(name_and_happiness_rating.keys())) <= 5:
        return 'Get Out Now!'
    
    return 'Nice Work Champ!'