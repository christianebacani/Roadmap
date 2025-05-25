# Question: Find the middle element
# Categories: 7 Kyu

def gimme(input_array: list[int]) -> int:
    sorted_input_array = sorted(input_array)
    return input_array.index(sorted_input_array[1])