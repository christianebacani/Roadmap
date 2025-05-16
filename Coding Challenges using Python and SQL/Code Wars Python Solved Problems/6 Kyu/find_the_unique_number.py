# Question: Find the unique number
# Categories: 6 Kyu

def find_uniq(arr: list[int]) -> int:
    distinct_arr = list(set(arr))
    
    for i in range(len(distinct_arr)):
        if arr.count(distinct_arr[i]) == 1:
            return distinct_arr[i]