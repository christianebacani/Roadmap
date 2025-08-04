# Question: Smallest value of an array
# Categories: 7 Kyu

def find_smallest(numbers: list[int], to_return: str) -> int:
    result = {
        'value': min(numbers),
        'index': numbers.index(min(numbers))
    }

    return result[to_return]