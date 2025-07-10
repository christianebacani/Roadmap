# Question: String doubles
# Categories: 7 Kyu

def doubles(s: str) -> str:    
    result = []

    for i in range(len(s)):
        if result == []:
            result.append(s[i])
            continue

        if result[-1] == s[i]:
            result = result[:-1]

        else:
            result.append(s[i])

    result = ''.join(result)
    return result