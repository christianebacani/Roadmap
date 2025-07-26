# Question: Printing Array elements with Comma delimiters
# Categories: 8 Kyu

def print_array(arr: list[str | int | float | bool]) -> list[str]:
    new_arr = []

    for i in range(len(arr)):
        new_arr.append(str(arr[i]))
    
    arr = new_arr
    arr = ','.join(arr)
    return arr