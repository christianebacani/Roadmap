# Question: Multiple of index
# Categories: 8 Kyu

def multiple_of_index(arr: list[int]) -> list[int]:
    new_arr = []

    for i in range(len(arr)):
        try:
            if i == 0 and arr[i] == 0:
                new_arr.append(arr[i])
                continue

            if arr[i] % i == 0:
                new_arr.append(arr[i])
        
        except ZeroDivisionError:
            continue

    arr = new_arr
    return arr