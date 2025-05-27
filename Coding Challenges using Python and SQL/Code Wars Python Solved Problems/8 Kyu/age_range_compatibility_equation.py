# Question: Age Range Compatibility Equation
# Categories: 8 Kyu
import math

def dating_range(age: int) -> str:
    if age <= 14:
        minimum_age_range = math.floor(age - 0.10 * age)
        maximum_age_range = math.floor(age + 0.10 * age)
    
    else:
        minimum_age_range = math.floor((age / 2) + 7)
        maximum_age_range = math.floor(2 * (age - 7))
    
    return f'{minimum_age_range}-{maximum_age_range}'