# Question: +1 Array
# Categories: 6 Kyu

def up_array(arr: list[int]) -> list[int] | None:
    if arr == []:
        return None

    sorted_arr_asc = sorted(arr)
    sorted_arr_desc = sorted(arr, reverse=True)

    if sorted_arr_asc[0] < 0:
        return None
    
    if sorted_arr_desc[0] >= 10:
        return None
    
    integer_string = ''

    for i in range(len(arr)):
        integer_string += str(arr[i])

    integer_string = int(integer_string) + 1
    integer_string = str(integer_string)
    result = []

    for i in range(len(integer_string)):
        result.append(int(integer_string[i]))
    
    if arr[0] != 0:
        return result
    
    if arr[0] == 0 and len(arr) == 1:
        return result
    
    if arr[0] == 0 and result == [1, 0]:
        return result

    if arr == [0, 1]:
        return result

    number_of_zero_prefix = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            break

        number_of_zero_prefix += 1

    for _ in range(number_of_zero_prefix):
        result.insert(0, 0)
    
    return result