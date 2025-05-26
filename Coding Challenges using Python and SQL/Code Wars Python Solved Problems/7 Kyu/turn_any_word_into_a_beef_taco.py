# Question: Turn any word into a beef taco
# Categories: 7 Kyu

def tacofy(word: str) -> list[str]:
    letter_and_ingredients = {
        'a': 'beef',
        'e': 'beef',
        'i': 'beef',
        'o': 'beef',
        'u': 'beef',
        't': 'tomato',
        'l': 'lettuce',
        'c': 'cheese',
        'g': 'guacamole',
        's': 'salsa'
    }
    result = []

    for i in range(len(word)):
        for letter, ingredient in letter_and_ingredients.items():
            if word[i].lower() == letter:
                result.append(ingredient)
                break
    
    result.insert(0, 'shell')
    result.append('shell')

    return result