# Question: You're a square!
# Categories: 7 Kyu
import math

def is_square(number: int) -> bool:
    try:
        square_root = math.sqrt(number)

    except ValueError:
        return False
    
    decimals = int(str(square_root).split('.')[1])

    if decimals > 0:
        return False
    
    return True