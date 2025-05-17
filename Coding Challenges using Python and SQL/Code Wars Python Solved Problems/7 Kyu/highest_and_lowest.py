# Question: Highest and Lowest
# Categories: 7 Kyu

def high_and_low(numbers: str) -> str:
    numbers = numbers.split()
    list_of_numbers = []

    for i in range(len(numbers)):
        list_of_numbers.append(int(numbers[i]))
    
    return f'{max(list_of_numbers)} {min(list_of_numbers)}'