# Question: Alternate Logic
# Categories: 7 Kyu

def alt_or(lst: list[bool]) -> bool | None:
    if lst == []:
        return None
    
    return True in lst