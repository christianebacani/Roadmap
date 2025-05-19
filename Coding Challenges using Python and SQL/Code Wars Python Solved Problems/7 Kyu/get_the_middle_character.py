# Question Get the Middle Character
# Categories: 7 Kyu

def get_middle(characters: str) -> str:
    if len(characters) % 2 == 0:
       return characters[(len(characters) // 2)  - 1] + characters[len(characters) // 2] 

    return characters[len(characters) // 2]