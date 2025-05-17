# Question: Isograms
# Categories: 7 Kyu

def is_isogram(string: str) -> bool:
    string = string.lower()

    for i in range(len(string)):
        if string.count(string[i]) != 1:
            return False
        
    return True