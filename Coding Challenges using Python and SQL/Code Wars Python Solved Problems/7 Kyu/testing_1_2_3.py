# Question: Testing 1-2-3
# Categories: 7 Kyu

def number(lines: list[str]) -> list[str]:
    if lines == []:
        return []

    for i in range(len(lines)):
        lines[i] = str(i + 1) + ': ' + lines[i]
    
    return lines