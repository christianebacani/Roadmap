# Question: Even numbers in an array
# Categories: 7 Kyu

def even_numbers(arr: list[int], n: int) -> list[int]:
    result = []

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            result.append(arr[i])
    
    return result[n * -1:]