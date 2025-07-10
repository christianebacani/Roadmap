# Question: Remove First and Last Character Part Two
# Categories: 7 Kyu

def array(string: str) -> str | None:
    if ',' not in string:
        return None
    
    if len(string.split(',')[1:-1]) == 0:
        return None
    
    result = string.split(',')[1:-1]
    result = ' '.join(result)

    return result