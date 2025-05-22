# Question: Array Leaders (Array Series #3)
# Categories: 7 Kyu

def array_leaders(numbers: list[int]) -> list[int]:
    list_of_array_leaders = []

    for i in range(len(numbers)):
        if numbers[i] > sum(numbers[i + 1:]):
            list_of_array_leaders.append(numbers[i])
    
    return list_of_array_leaders