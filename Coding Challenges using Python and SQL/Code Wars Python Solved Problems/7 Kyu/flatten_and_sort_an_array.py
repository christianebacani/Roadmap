# Question: Flatten and sort an array
# Categories: 7 Kyu

def flatten_and_sort(array: list[list[int]]) -> list[int]:
    '''
        Convert the two-dimensional array to one dimension
        and sort the array
    '''
    array_one_dimension = []

    for i in range(len(array)):
        for j in range(len(array[i])):
            array_one_dimension.append(array[i][j])
    
    array_one_dimension.sort()
    return array_one_dimension