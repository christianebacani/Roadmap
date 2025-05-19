# Question: The Office II - Boredom Score
# Categories: 7 Kyu

def boredom(staff: dict[str, int]) -> str:
    department_and_boredom_score = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }
    total_score = 0

    for _, department in staff.items():
        total_score += department_and_boredom_score[department]
    
    if total_score <= 80:
        return 'kill me now'

    elif total_score > 80 and total_score < 100:
        return 'i can handle this'

    return 'party time!!'