# Question: Cat years, Dog years
# Categories: 8 Kyu

def human_years_cat_years_dog_years(human_years: int) -> int:
    humanYears = 0
    catYears = 0
    dogYears = 0

    for year in range(1, human_years + 1):
        humanYears += 1

        if year == 1:
            catYears += 15
            dogYears += 15
        
        elif year == 2:
            catYears += 9
            dogYears += 9
        
        else:
            catYears += 4
            dogYears += 5
    
    return [humanYears, catYears, dogYears]