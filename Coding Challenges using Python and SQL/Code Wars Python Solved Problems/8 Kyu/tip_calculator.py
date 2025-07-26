# Question: Tip Calculator
# Categories: 8 Kyu

import math

def calculate_tip(amount: int, rating: str) -> int | str:
    ratings_and_tip_pct = {
        'terrible': 0,
        'poor': 5,
        'good': 10,
        'great': 15,
        'excellent': 20
    }

    if rating.lower() not in ratings_and_tip_pct:
        return 'Rating not recognised'
    
    if ratings_and_tip_pct[rating.lower()] == 0:
        return 0
    
    tip = (ratings_and_tip_pct[rating.lower()] / 100) * amount
    tip = math.ceil(tip)

    return tip