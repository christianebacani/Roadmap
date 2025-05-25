# Question: Digits Average
# Categories: 7 Kyu
import math

def digits_average(x: int) -> int:
    number_string = str(x)

    while len(number_string) != 1:
        mean_of_consecutive_digits = ''

        for i in range(1, len(number_string)):
            previous_digit = number_string[i - 1]
            current_digit = number_string[i]

            mean_of_consecutive_digits += str(math.ceil((int(previous_digit) + int(current_digit)) / 2))

        number_string = mean_of_consecutive_digits
    
    return int(number_string)