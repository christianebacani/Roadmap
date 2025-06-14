# Question: Remember
# Categories: 6 Kyu

def remember(str_: str) -> list[str]:
    result = []

    for i in range(len(str_)):
        if str_[i] in result:
            continue

        if str_[i] in str_[:i]:
            result.append(str_[i])
    
    return result