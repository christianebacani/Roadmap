# Question: You only need one - Beginner
# Categories: 8 Kyu

def check(sequence: list[str | int], elem: str | int) -> bool:
    if elem in sequence:
        return True
    
    return False