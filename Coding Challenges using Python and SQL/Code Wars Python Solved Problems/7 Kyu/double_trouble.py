# Question: Double trouble
# Categories: 7 Kyu

def consecutive_num_that_sums_to_target(arr: list[int], target: int) -> bool:
    for i in range(len(arr)):
        if i == len(arr) - 1:
            continue

        if (arr[i] + arr[i + 1]) == target:
            return True
    
    return False

def trouble(x: list[int], t: int) -> list[int]:
    while consecutive_num_that_sums_to_target(x, t) is True:
        for i in range(len(x)):
            if i == len(x) - 1:
                continue

            if (x[i] + x[i + 1]) == t:
                index_to_remove = i + 1
                break
        
        x.pop(index_to_remove)

    return x