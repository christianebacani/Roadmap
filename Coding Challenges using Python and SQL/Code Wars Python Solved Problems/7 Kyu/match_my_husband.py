# Question: Match My Husband
# Categories: 7 Kyu

def match(usefulness: list[int], months: int) -> str:
    usefulness_rating = sum(usefulness)
    needs_rating = 100 * (0.85 ** months)
    
    if usefulness_rating >= needs_rating:
        return 'Match!'
    
    return 'No match!'