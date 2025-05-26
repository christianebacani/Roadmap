# Question: Jumping Number (Special Numbers Series #4)
# Categories: 7 Kyu

def jumping_number(number: int) -> str:
    number_string = str(number)
    
    if len(number_string) == 1:
        return 'Jumping!!'

    for i in range(1, len(number_string)):
        previous_digit = number_string[i - 1]
        current_digit = number_string[i]

        if abs(int(previous_digit) - int(current_digit)) != 1:
            return 'Not!!'
    
    return 'Jumping!!'