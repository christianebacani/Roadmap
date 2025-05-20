# Question: Fold an array
# Categories: 6 Kyu

def fold_array(array: list[int], number_of_folds: int) -> list[int]:
    initial_number_of_folds = 0

    while initial_number_of_folds < number_of_folds:
        if len(array) == 1:
            initial_number_of_folds += 1
            continue

        index_delimiter = len(array) // 2

        if len(array) % 2 != 0:
            first_half = array[:index_delimiter]
            middle_element = array[index_delimiter]
            second_half = array[index_delimiter + 1:][::-1]
            
            for i in range(len(first_half)):
                first_half[i] = first_half[i] + second_half[0]
                second_half = second_half[1:]
            
            array = first_half
            array.append(middle_element)
        
        else:
            first_half = array[:index_delimiter]
            second_half = array[index_delimiter:][::-1]

            for i in range(len(first_half)):
                first_half[i] = first_half[i] + second_half[0]
                second_half = second_half[1:]
            
            array = first_half
        
        initial_number_of_folds += 1
    
    return array