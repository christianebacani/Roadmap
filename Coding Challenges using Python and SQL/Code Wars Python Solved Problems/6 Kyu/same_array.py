# Question: Same Array?
# Categories: 6 Kyu

def sort_array(arr: list[list[int]]) -> list[list[int]]:
    for i in range(len(arr)):
        arr[i] = sorted(arr[i])
    
    return sorted(arr)

def same(first_arr: list[list[int]], second_arr: list[list[int]]) -> bool:
    if first_arr == [] and second_arr == []:
        return True
    
    if len(first_arr) != len(second_arr):
        return False
    
    first_arr = sort_array(first_arr)
    second_arr = sort_array(second_arr)
    total_array = len(first_arr)

    for i in range(total_array):
        try:
            if first_arr[i] != second_arr[i]:
                return False
        
        except IndexError:
            return False
    
    return True