# Question: Small enough? - Beginner
# Categories: 7 Kyu

def small_enough(array: list[int], limit: int) -> bool:
    for i in range(len(array)):
        if array[i] > limit:
            return False
    
    return True