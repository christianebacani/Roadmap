# Question: Shortest Distance to a Character
# Categories: 6 Kyu

def shortest_to_char(s: str, c: str) -> list[int]:
    if s == '' or c == '':
        return []
    
    indices_of_letter_c = []

    for i in range(len(s)):
        if s[i] == c:
            indices_of_letter_c.append(i)

    if indices_of_letter_c == []:
        return []

    result = []
    
    for i in range(len(s)):
        distances = []

        for j in range(len(indices_of_letter_c)):
            distances.append(abs(i - indices_of_letter_c[j]))

        result.append(min(distances, default=0))
    
    return result