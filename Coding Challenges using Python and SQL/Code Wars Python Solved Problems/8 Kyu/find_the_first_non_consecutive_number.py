# Question: Find the first non-consecutive number
# Categories: 8 Kyu

def first_non_consecutive(arr: int) -> int:
    for i in range(1, len(arr)):
        previous_number = arr[i - 1]
        current_number = arr[i]

        if (current_number - previous_number) != 1:
            return current_number

    return None