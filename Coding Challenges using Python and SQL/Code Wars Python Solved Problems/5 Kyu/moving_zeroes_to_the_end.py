# Question: Moving Zeroes To The End
# Categories: 5 Kyu

def move_zeros(lst: list[int]) -> list[int]:
    non_zero_numbers = []
    zero_numbers = []

    for i in range(len(lst)):
        if lst[i] > 0:
            non_zero_numbers.append(lst[i])
        
        else:
            zero_numbers.append(lst[i])
    
    return non_zero_numbers + zero_numbers