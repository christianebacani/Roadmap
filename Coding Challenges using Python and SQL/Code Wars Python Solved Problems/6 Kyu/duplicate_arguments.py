# Question: Duplicate Arguments
# Categories: 6 Kyu

def solution(*args) -> bool:
    elements = []

    for element in args:
        elements.append(element)
    
    if len(set(elements)) != len(elements):
        return True
    
    return False