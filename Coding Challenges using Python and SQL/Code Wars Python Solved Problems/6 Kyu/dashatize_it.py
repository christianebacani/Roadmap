# Question: Dashatize it
# Categories: 6 Kyu

def dashatize(n: int) -> str:
    n = str(n)
    result = []

    for i in range(len(n)):
        if n[i] == '-':
            continue

        if int(n[i]) % 2 == 0:
            result.append(n[i])
            continue
        
        if result == []:
            result.append('-')
            result.append(n[i])
            result.append('-')
            continue
        
        if '-' in result[-1]:
            result.append(n[i])
            result.append('-')
            continue
    
        result.append('-')
        result.append(n[i])
        result.append('-')

    result = ''.join(result)
    
    if result[0] == '-':
        result = result[1:]
    
    if result[-1] == '-':
        result = result[:-1]
    
    return result