# Question: What's the real floor?
# Categories: 8 Kyu

def get_real_floor(floor: int) -> int:
    if floor <= 0:
        return floor

    elif floor > 0 and floor < 13:
        return floor - 1
    
    else:
        return floor - 2