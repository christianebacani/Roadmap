# Question: Validate Credit Card Number
# Categories: 6 Kyu

def double_elements(arr: list[str]) -> list[str]:
    arr = arr[::-1]
    result = []
    
    for i in range(len(arr)):
        if i % 2 != 0:
            result.append(str(int(arr[i]) * 2))

        else:
            result.append(arr[i])
    
    result = result[::-1]
    return result

def add_digits_if_contains_more_than_one_digit(arr: list[str]) -> list[str]:
    result = []

    for i in range(len(arr)):
        if len(arr[i]) == 1:
            result.append(arr[i])
            continue
        
        total = 0

        for j in range(len(arr[i])):
            total += int(arr[i][j])

        arr[i] = str(total)
        result.append(arr[i])
    
    return result

def validate(number: int) -> bool:
    number = list(str(number))
    doubled_number = double_elements(number)
    added_digits_number = add_digits_if_contains_more_than_one_digit(doubled_number)
    added_digits_number = [int(num) for num in added_digits_number]

    if sum(added_digits_number) % 10 == 0:
        return True
    
    return False