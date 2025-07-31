# Question: Are they the 'same'?
# Categories: 6 Kyu

def comp(array1: list[int], array2: list[int]) -> list[int]:
    if array1 is None:
        return False
    
    if array2 is None:
        return False

    if isinstance(array1, set):
        array1 = list(array1)
    
    if isinstance(array2, set):
        array2 = list(array2)

    if (array1 == [] and array2 != []) or (array1 != [] and array2 == []):
        return False

    for i in range(len(array1)):
        array1[i] = array1[i] * array1[i]
    
    array1.sort()
    array2.sort()

    return array1 == array2