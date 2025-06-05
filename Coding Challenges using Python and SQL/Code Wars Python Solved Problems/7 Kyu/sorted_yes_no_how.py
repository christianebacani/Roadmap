# Question: Sorted? yes? no? how?
# Categories: 7 Kyu

def is_sorted_and_how(arr: list[int]) -> str:
    if sorted(arr) == arr:
        return 'yes, ascending'

    elif sorted(arr, reverse=True) == arr:
        return 'yes, descending'
    
    else:
        return 'no'