# Question: Sort the odd
# Categories: 6 Kyu

def sort_array(source_array: list[int]) -> list[int]:
    odd_elements = []
    
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            odd_elements.append(source_array[i])

    odd_elements = sorted(odd_elements)

    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd_elements[0]
            odd_elements = odd_elements[1:]
    
    return source_array