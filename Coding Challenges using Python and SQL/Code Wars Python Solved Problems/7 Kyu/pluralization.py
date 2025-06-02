# Question: Pluralization
# Categories: 7 Kyu

def pluralize(word: str) -> str:
    first_singular_noun_suffixes = [
        's', 'x', 'z', 'ch', 'sh'
    ]
    second_singular_noun_suffixes = [
        'y'
    ]

    contains_first_singular_noun_suffix = False
    contains_second_singular_noun_suffix = False

    for i in range(len(first_singular_noun_suffixes)):
        if word.endswith(first_singular_noun_suffixes[i]):
            word = word + 'es'
            contains_first_singular_noun_suffix = True
            break
    
    if contains_first_singular_noun_suffix:
        return word
    
    for i in range(len(second_singular_noun_suffixes)):
        if word[-2].lower() not in 'aeiou' and word[-1] == second_singular_noun_suffixes[i]:
            word = word[:-1] + 'ies'
            contains_second_singular_noun_suffix = True
            break

    if contains_second_singular_noun_suffix:
        return word
    
    return word + 's'