# Question: Maximum Gap (Array Series #4)
# Categories: 7 Kyu

def max_gap(numbers: list[int]) -> int:
    numbers.sort()
    differences = []

    for i in range(1, len(numbers)):
        previous_number = numbers[i - 1]
        current_number = numbers[i]

        differences.append(abs(previous_number - current_number))
    
    return max(differences)