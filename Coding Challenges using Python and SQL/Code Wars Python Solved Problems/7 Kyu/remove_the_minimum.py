# Question: Remove the minimum
# Categories; 7 Kyu

def remove_smallest(numbers: list[int]) -> list[int]:
    if numbers == []:
        return []
    
    index_of_minimum_number = numbers.index(min(numbers))
    result = []

    for i in range(len(numbers)):
        if i != index_of_minimum_number:
            result.append(numbers[i])
    
    return result