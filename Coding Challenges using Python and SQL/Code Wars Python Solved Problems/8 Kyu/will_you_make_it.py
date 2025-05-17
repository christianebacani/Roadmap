# Question: Will you make it?
# Categories 8 Kyu

def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    if mpg * fuel_left >= distance_to_pump:
        return True
    
    return False