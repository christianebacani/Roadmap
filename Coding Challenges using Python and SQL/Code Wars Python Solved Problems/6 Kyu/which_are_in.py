# Question: Which are in?
# Categories: 6 Kyu

def in_array(arr1: list[str], arr2: list[str]) -> list[str]:
    result = []

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] in arr2[j]:
                result.append(arr1[i])
                break
    
    result = sorted(list(set(result)))

    return result