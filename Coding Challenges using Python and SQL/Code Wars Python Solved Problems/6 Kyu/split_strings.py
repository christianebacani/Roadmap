# Question: Split Strings
# Categories: 6 Kyu

def solution(s: str) -> list[str]:
    splitted_strings = []

    for i in range(0, len(s), 2):
        splitted_string = s[i : i + 2]

        if len(splitted_string) == 2:
            splitted_strings.append(splitted_string)
        
        else:
            splitted_string = splitted_string + '_'
            splitted_strings.append(splitted_string)
    
    return splitted_strings