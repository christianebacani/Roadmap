# Question: Is Integer Array?
# Categories: 6 Kyu

def is_int_array(arr: list[int | float | None | bool | str]) -> bool:
    if arr == []:
        return True
    
    if not isinstance(arr, list):
        return False

    for i in range(len(arr)):
        if arr[i] is None:
            return False
        
        if arr[i] is True or arr[i] is False:
            return False

        if not isinstance(arr[i], (int, float)):
            return False

        if isinstance(arr[i], int):
            continue

        if int(str(arr[i]).split('.')[1]) > 0:
            return False

    return True