# Question: Monotone travel
# Categories: 7 Kyu

def is_monotone(heights: list[int | float]) -> bool:
    if heights == []:
        return True
    
    return sorted(heights) == heights