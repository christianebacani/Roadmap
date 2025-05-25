# Question: Balanced Number (Special Numbers Series # 1)
# Categories: 7 Kyu

def balanced_num(number: int) -> str:
    number_string = str(number)

    if len(number_string) % 2  == 0:
        first_middle_index = (len(number_string) // 2) - 1
        second_middle_index = len(number_string) // 2

        left_side = number_string[:first_middle_index]
        right_side = number_string[second_middle_index + 1:]
    
    else:
        middle_index = len(number_string) // 2
        
        left_side = number_string[:middle_index]
        right_side = number_string[middle_index + 1:]
    
    left_side_sum, right_side_sum = 0, 0

    for i in range(len(left_side)):
        left_side_sum += int(left_side[i])
    
    for i in range(len(right_side)):
        right_side_sum += int(right_side[i])
    
    if left_side_sum == right_side_sum:
        return 'Balanced'
    
    return 'Not Balanced'