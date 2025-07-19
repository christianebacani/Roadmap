# Question: Logical calculator
# Categories: 8 Kyu

def logical_calc(array: list[bool], op: str) -> bool:
    if len(array) == 1:
        return array[0]
    
    if op == 'AND':
        current_result = array[0] and array[1]
    
    elif op == 'OR':
        current_result = array[0] or array[1]
    
    else:
        current_result = array[0] ^ array[1]
    
    array = array[2:]
    
    while len(array) > 0:
        if op == 'AND':
            current_result = current_result and array[0]
        
        elif op == 'OR':
            current_result = current_result or array[0]

        else:
            current_result = current_result ^ array[0]
        
        array = array[1:]
    
    answer = current_result

    return answer