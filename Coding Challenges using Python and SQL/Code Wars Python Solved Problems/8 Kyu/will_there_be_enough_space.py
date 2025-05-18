# Question: Will there be enough space?
# Categories: 8 Kyu

def enough(capacity: int, onboard: int, waiting: int) -> int:
    if onboard + waiting <= capacity:
        return 0
        
    return (onboard + waiting) - capacity