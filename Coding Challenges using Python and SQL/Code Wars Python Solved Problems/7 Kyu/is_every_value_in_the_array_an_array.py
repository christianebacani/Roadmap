# Question: Is every value in the array an array?
# Categories: 7 Kyu

def arr_check(arr: list[list[int] | list[str] | str| int | dict[str, str] | dict[int, int]]) -> bool:
    for i in range(len(arr)):
        if not isinstance(arr[i], list):
            return False
    
    return True