# Question: I love you, a little, a lot, passionately ... not at all
# Categories: 8 Kyu

def how_much_i_love_you(number_of_petals: int) -> str:
    phrases = [
        'I love you', 'a little', 'a lot',
        'passionately', 'madly', 'not at all'
    ]

    if number_of_petals - 1 > len(phrases) - 1:
        return phrases[(number_of_petals - 1) % len(phrases)]
    
    return phrases[number_of_petals - 1]