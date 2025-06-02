# Question: Format to the 2nd
# Categories: 7 Kyu

def print_nums(*args) -> str:
    numbers = []

    for i in range(len(args)):
        numbers.append(str(args[i]))
    
    maximum_length_of_a_number = 0

    for i in range(len(numbers)):
        if len(numbers[i]) > maximum_length_of_a_number:
            maximum_length_of_a_number = len(numbers[i])

    result = []

    for i in range(len(numbers)):
        prefix = abs(maximum_length_of_a_number - len(numbers[i])) * '0'
        numbers[i] = prefix + numbers[i]

        result.append(numbers[i])
    
    return '\n'.join(result)