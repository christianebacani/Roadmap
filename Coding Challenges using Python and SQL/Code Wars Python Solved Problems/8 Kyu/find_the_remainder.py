# Question: Find the Remainder
# Categories: 8 Kyu

def remainder(a: int, b: int) -> int | None:
    if min([a, b]) == 0:
        return None
    
    if min([a, b]) != 0 and 0 in [a, b]:
        return 0
    
    return max([a, b]) % min([a, b])