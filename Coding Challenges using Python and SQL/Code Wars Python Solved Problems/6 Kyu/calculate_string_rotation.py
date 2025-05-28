# Question: Calculate String Rotation
# Categories: 6 Kyu

def shifted_diff(first: str, second: str) -> int:
    total_number_of_shifts = len(first)
    i = 0
    count = 0

    while i < total_number_of_shifts:
        if first != second:
            first = first[-1] + first[:-1]
            i += 1
            count += 1
        
        else:
            break
    
    if first != second:
        return -1
    
    return count