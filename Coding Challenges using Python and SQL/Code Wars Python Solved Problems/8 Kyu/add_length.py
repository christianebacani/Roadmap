# Question: Add Length
# Categories: 8 Kyu

def add_length(str_: str) -> list[str]:
    str_ = str_.split()
    result = []
    
    for i in range(len(str_)):
        result.append(str_[i] + ' ' + str(len(str_[i])))
    
    return result