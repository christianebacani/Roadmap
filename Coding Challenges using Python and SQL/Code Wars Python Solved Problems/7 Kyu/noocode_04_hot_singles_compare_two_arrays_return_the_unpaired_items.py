# Question: noobCode 04: HOT SINGLES...compare two arrays, return the unpaired items !
# Categories: 7 Kyu

def hot_singles(arr1: list[int | str], arr2: list[int | str]) -> list[int | str]:
    result = []

    for i in range(len(arr1)):
        if arr1[i] in arr2:
            continue

        if arr1[i] not in result:
            result.append(arr1[i])

    for i in range(len(arr2)):
        if arr2[i] in arr1:
            continue

        if arr2[i] not in result:
            result.append(arr2[i])

    return result