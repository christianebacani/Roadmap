# Question: Divide and Conquer
# Categories: 7 Kyu

def div_con(x: list[int | str]) -> int:
    total_non_string_integers, total_string_integers = 0, 0

    for i in range(len(x)):
        if isinstance(x[i], int):
            total_non_string_integers += x[i]
        
        else:
            total_string_integers += int(x[i])
    
    result = total_non_string_integers - total_string_integers
    return result