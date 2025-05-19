# Question: List Filtering
# Categories: 7 Kyu

def filter_list(arr: list[str | int]) -> list[int]:
    filtered_arr = []

    for i in range(len(arr)):
        if isinstance(arr[i], int):
            filtered_arr.append(arr[i])
    
    return filtered_arr