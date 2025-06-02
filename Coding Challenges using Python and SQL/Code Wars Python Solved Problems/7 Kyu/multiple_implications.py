# Question: Multiple implications
# Categories: 7 Kyu

def mult_implication(lst: list[bool]) -> bool | None:
    if lst == []:
        return None
    
    if len(lst) == 1:
        return lst[0]
    
    implication = None

    if lst[0] is True and lst[1] is False:
        implication = False

    else:
        implication = True
    
    if len(lst) == 2:
        return implication
    
    for i in range(2, len(lst)):
        if implication is True and lst[i] is False:
            implication = False

        else:
            implication = True
    
    return implication