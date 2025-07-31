# Question: String Templates - Bug Fixing #5
# Categories: 8 Kyu

def build_string(*args) -> str:
    result = []

    for i in range(len(args)):
        result.append(args[i])
    
    result = ', '.join(result)
    return f'I like {result}!'