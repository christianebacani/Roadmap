# Question: Find the stray number
# Categories: 7 Kyu

def stray(arr: list[int]) -> list[int]:
    distinct_arr = list(set(arr))

    for i in range(len(distinct_arr)):
        if arr.count(distinct_arr[i]) == 1:
            return distinct_arr[i]