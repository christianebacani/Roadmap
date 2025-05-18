# Question: CamelCase Method
# Categories: 6 Kyu

def camel_case(characters: str) -> str:
    characters = characters.split()
    characters = [word.capitalize() for word in characters]

    return ''.join(characters)