# Question: Inverting a Hash
# Categories: 7 Kyu

def invert_hash(dictionary: dict[str | int, str | int]):
    result = {}

    for value in list(dictionary.values()):
        result[value] = None
    
    for key, value in dictionary.items():
        result[value] = key
    
    return result