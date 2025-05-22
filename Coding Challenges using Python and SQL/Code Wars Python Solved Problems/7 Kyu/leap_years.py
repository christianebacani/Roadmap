# Question: Leap Years
# Categories: 7 Kyu

def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False
    
    if year % 100 != 0:
        return True
    
    if year % 400 == 0:
        return True
    
    return False