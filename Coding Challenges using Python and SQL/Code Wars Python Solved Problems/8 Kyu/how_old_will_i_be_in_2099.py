# Question: How old will I be in 2099?
# Categories: 8 Kyu

def calculate_age(year_of_birth: int, current_year: int) -> str:
    if year_of_birth < current_year:
        total_years = current_year - year_of_birth

        if total_years == 1:
            return 'You are 1 year old.'

        return f'You are {total_years} years old.'

    total_years = year_of_birth - current_year

    if total_years == 0:
        return 'You were born this very year!'

    elif total_years == 1:
        return 'You will be born in 1 year.'
    
    return f'You will be born in {total_years} years.'