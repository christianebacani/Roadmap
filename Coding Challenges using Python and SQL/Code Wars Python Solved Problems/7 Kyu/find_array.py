# Question: Find array
# Categories: 7 Kyu

def find_array(arr1: list[int | str], arr2: list[int]) -> list[int | str]:
    result = []

    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr2[i] == j:
                result.append(arr1[j])
    
    return result