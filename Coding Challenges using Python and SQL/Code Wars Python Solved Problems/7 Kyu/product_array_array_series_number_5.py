# Question: Product Array (Array Series #5)
# Categories: 7 Kyu

def product_array(numbers: list[int]) -> list[int]:
    result = []

    for i in range(len(numbers)):
        total = 1
        previous_numbers = numbers[:i]
        next_numbers = numbers[i + 1:]

        if previous_numbers != []:
            for j in range(len(previous_numbers)):
                total *= previous_numbers[j]
        
        if next_numbers != []:
            for j in range(len(next_numbers)):
                total *= next_numbers[j]
        
        result.append(total)

    return result