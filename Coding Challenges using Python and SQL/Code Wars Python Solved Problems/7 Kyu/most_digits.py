# Question: Most digits
# Categories: 7 Kyu

def find_longest(arr: list[int]) -> int:
    total_number_of_digits = 0

    for i in range(len(arr)):
        if len(str(arr[i])) > total_number_of_digits:
            total_number_of_digits = len(str(arr[i]))
    
    for i in range(len(arr)):
        if len(str(arr[i])) == total_number_of_digits:
            return arr[i]