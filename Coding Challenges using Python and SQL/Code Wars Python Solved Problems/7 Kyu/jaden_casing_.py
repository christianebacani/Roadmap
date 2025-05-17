# Question: Jaden Casing Strings
# Categories: 7 Kyu

def to_jaden_case(string: str) -> str:
    string = string.split()

    for i in range(len(string)):
        string[i] = string[i].capitalize()
    
    return ' '.join(string)