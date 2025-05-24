# Question: Lost number in number sequence
# Categories: 7 Kyu

def find_deleted_number(original_arr: list[int], mixed_arr: list[int]) -> int:
    for i in range(len(original_arr)):
        if original_arr[i] not in mixed_arr:
            return original_arr[i]

    return 0