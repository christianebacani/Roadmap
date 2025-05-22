# Question: If you can read this...
# Categories: 6 Kyu

def to_nato(words : str) -> str:
    nato = {
        'A': 'Alfa',
        'B': 'Bravo',
        'C': 'Charlie',
        'D': 'Delta',
        'E': 'Echo',
        'F': 'Foxtrot',
        'G': 'Golf',
        'H': 'Hotel',
        'I': 'India',
        'J': 'Juliett',
        'K': 'Kilo',
        'L': 'Lima',
        'M': 'Mike',
        'N': 'November',
        'O': 'Oscar',
        'P': 'Papa',
        'Q': 'Quebec',
        'R': 'Romeo',
        'S': 'Sierra',
        'T': 'Tango',
        'U': 'Uniform',
        'V': 'Victor',
        'W': 'Whiskey',
        'X': 'Xray',
        'Y': 'Yankee',
        'Z': 'Zulu'
    }
    result = []

    for i in range(len(words)):
        if words[i] == ' ':
            continue

        if not words[i].isalpha():
            result.append(words[i])
        
        else:
            result.append(nato[words[i].upper()])
    
    return ' '.join(result)