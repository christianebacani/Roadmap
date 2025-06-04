# Question: Max-min arrays
# Categories: 7 Kyu

def solve(arr: list[int]) -> list[int]:
    non_increasing_arr = sorted(arr, reverse=True)
    non_decreasing_arr = sorted(arr)
    
    total_length = len(non_increasing_arr)
    result = []

    for i in range(total_length):
        if non_increasing_arr[i] not in result:
            result.append(non_increasing_arr[i])
        
        if non_decreasing_arr[i] not in result:
            result.append(non_decreasing_arr[i])
    
    return result