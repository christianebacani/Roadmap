# Question: Count of positives / sum of negatives
# Categories: 8 Kyu

def count_positives_sum_negatives(arr: list[int]) -> list[int]:
    if arr == []:
        return []

    number_of_positive_number = 0
    total_sum_of_negative_number = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            continue

        if arr[i] > 0:
            number_of_positive_number += 1
        
        else:
            total_sum_of_negative_number += arr[i]
    
    return [number_of_positive_number, total_sum_of_negative_number]