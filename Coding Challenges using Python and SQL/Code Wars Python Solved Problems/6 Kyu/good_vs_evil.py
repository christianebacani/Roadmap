# Question: Good vs Evil
# Categories: 6 Kyu

def good_vs_evil(good: str, evil: str) -> str:
    good_races_worth = [1, 2, 3, 3, 4, 10]
    evil_races_worth = [1, 2, 2, 2, 3, 5, 10]

    good_races_total_worth = 0
    evil_races_total_worth = 0

    for i in range(len(good.split())):
        good_races_total_worth += (int(good.split()[i]) * good_races_worth[i])
    
    for i in range(len(evil.split())):
        evil_races_total_worth += (int(evil.split()[i]) * evil_races_worth[i])

    if good_races_total_worth > evil_races_total_worth:
        return 'Battle Result: Good triumphs over Evil'

    elif evil_races_total_worth > good_races_total_worth:
        return 'Battle Result: Evil eradicates all trace of Good'

    else:
        return 'Battle Result: No victor on this battle field'