# Question: Indexed capitalization
# Categories: 7 Kyu

def capitalize(s: str, ind: list[int]) -> str:
    lst = list(s)

    for i in range(len(ind)):
        try:
            lst[ind[i]] = lst[ind[i]].upper()

        except IndexError:
            pass
    
    s = ''.join(lst)
    return s