# Question: Sort Out The Men From Boys
# Categories: 7 Kyu

def men_from_boys(arr: list[int]) -> list[int]:
    even_numbers = []
    odd_numbers = []

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_numbers.append(arr[i])
        
        else:
            odd_numbers.append(arr[i])
    
    result = []
    result.extend(sorted(list(set(even_numbers))))
    result.extend(sorted(list(set(odd_numbers)), reverse=True))

    return result