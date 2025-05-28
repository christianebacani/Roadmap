# Question: Balance the arrays
# Categories: 6 Kyu

def balance(arr1: list[str], arr2: list[str]) -> bool:
    distinct_arr1 = list(set(arr1))
    distinct_arr2 = list(set(arr2))

    frequency_of_distinct_elements_from_arr1 = []
    frequency_of_distinct_elements_from_arr2 = []

    for i in range(len(distinct_arr1)):
        frequency_of_distinct_elements_from_arr1.append(arr1.count(distinct_arr1[i]))
    
    for i in range(len(distinct_arr2)):
        frequency_of_distinct_elements_from_arr2.append(arr2.count(distinct_arr2[i]))
    
    return sorted(frequency_of_distinct_elements_from_arr1) == sorted(frequency_of_distinct_elements_from_arr2)