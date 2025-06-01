# Question: sum2total
# Categories: 7 Kyu

def total(arr: list[int]) -> int:
    while len(arr) != 1:
        new_arr = []

        for i in range(1, len(arr)):
            new_arr.append(arr[i - 1] + arr[i])
        
        arr = new_arr
    
    return arr[0]