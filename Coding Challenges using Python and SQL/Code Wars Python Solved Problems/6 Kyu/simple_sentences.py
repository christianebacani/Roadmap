# Question: Simple Sentences
# Categories: 6 Kyu

def make_sentences(parts: list[str]) -> str:
    result = []

    for i in range(len(parts)):
        if parts[i] != ',':
            result.append(parts[i])
            result.append(' ')
            continue

        if result[-1] == ' ':
            result[-1] = ','
            result.append(' ')
        
        else:
            result.append(',')
            result.append(' ')

    result = ''.join(result)
    formatted_result = ''

    for i in range(len(result)):
        if result[i] == '.':
            continue

        formatted_result += result[i]

    formatted_result = formatted_result.strip()
    return formatted_result + '.'