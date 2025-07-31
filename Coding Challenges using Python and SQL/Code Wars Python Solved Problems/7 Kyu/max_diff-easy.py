# Question: max diff - easy
# Categories: 7 Kyu

def max_diff(lst: list[int]) -> int:
    if lst == []:
        return 0
    
    lst.sort()
    lst.reverse()
    
    return lst[0] - lst[-1]