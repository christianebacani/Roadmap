# Question: Mumbling
# Categories: 7 Kyu

def accum(st: str) -> str:
    result = ''

    for index, char in enumerate(st):
        index += 1

        if result == '':
            result += (char * index).capitalize()
        
        else:
            result += ('-' + (char * index).capitalize())
    
    return result