# Question: Odd or Even?
# Categories: 7 Kyu

def odd_or_even(arr: list[int]) -> str:
    if sum(arr) % 2 == 0:
        return 'even'
    
    return 'odd'