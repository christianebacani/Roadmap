# Question: Highest Rank Number in an Array
# Categories: 6 Kyu

def highest_rank(arr: list[int]) -> int:
    distinct_arr = list(set(arr))
    highest_frequency = 0
    
    for i in range(len(distinct_arr)):
        if arr.count(distinct_arr[i]) > highest_frequency:
            highest_frequency = arr.count(distinct_arr[i])
    
    most_frequent_element = []

    for i in range(len(distinct_arr)):
        if arr.count(distinct_arr[i]) == highest_frequency:
            most_frequent_element.append(distinct_arr[i])
    
    return max(most_frequent_element)