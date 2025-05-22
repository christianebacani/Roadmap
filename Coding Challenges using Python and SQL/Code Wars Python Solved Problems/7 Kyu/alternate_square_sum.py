# Question: Alternate Square Sum
# Categories: 7 Kyu

def alternate_sq_sum(arr: list[int]) -> int:
    odd_position_elements = []
    even_position_elements = []
    
    for i in range(len(arr)):
        if i % 2 == 0:
            odd_position_elements.append(arr[i])
        
        else:
            even_position_elements.append(arr[i])
    
    even_position_elements = [num ** 2 for num in even_position_elements]

    return sum(odd_position_elements) + sum(even_position_elements)