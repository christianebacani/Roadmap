# Question: Tail Swap
# Categories: 7 Kyu

def tail_swap(arr: list[str]) -> list[str]:
    result = []

    first_element_head = arr[0].split(':')[0]
    first_element_tail = arr[0].split(':')[1]
    
    second_element_head = arr[1].split(':')[0]
    second_element_tail = arr[1].split(':')[1]

    result.append(f'{first_element_head}:{second_element_tail}')
    result.append(f'{second_element_head}:{first_element_tail}')
    
    return result