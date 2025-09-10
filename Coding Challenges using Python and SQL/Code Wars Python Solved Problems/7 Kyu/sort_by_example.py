# Question: Sort by Example
# Categories: 7 Kyu

def example_sort(arr: list[int], example_arr: list[int]) -> list[int]:
    result = []

    for i in range(len(example_arr)):
        while example_arr[i] in arr:
            for j in range(len(arr)):
                if example_arr[i] == arr[j]:
                    result.append(arr[j])
                    del arr[j]
                    break
    
    return result