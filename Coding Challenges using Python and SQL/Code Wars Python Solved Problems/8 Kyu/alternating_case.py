# Question: altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Categories: 8 Kyu

def to_alternating_case(characters: str) -> str:
    characters = list(characters)

    for i in range(len(characters)):
        if characters[i].islower():
            characters[i] = characters[i].upper()

        else:
            characters[i] = characters[i].lower()
    
    return ''.join(characters)