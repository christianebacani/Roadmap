# Question: Alan Partridge I - Partridge Watch
# Categories: 7 Kyu

def part(arr: list[str]) -> str:
    related_terms = [
        'Partridge',
        'PearTree',
        'Chat',
        'Dan',
        'Toblerone',
        'Lynn',
        'AlphaPapa',
        'Nomad'
    ]

    related_terms_found = 0

    for i in range(len(arr)):
        if arr[i] in related_terms:
            related_terms_found += 1
    
    if related_terms_found == 0:
        return 'Lynn, I\'ve pierced my foot on a spike!!'
    
    return 'Mine\'s a Pint' + ('!' * related_terms_found)