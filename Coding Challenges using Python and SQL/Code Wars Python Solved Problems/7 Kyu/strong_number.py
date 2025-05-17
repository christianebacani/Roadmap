# Question: Strong Number (Special Numbers Series # 2)
# Categories: 7 Kyu

def strong_num(number: int) -> str:
    sum_of_its_factorial_digit = 0
    number_string = str(number)

    for i in range(len(number_string)):
        factorial = 1

        for j in range(1, int(number_string[i]) + 1):
            factorial *= j
        
        sum_of_its_factorial_digit += factorial
    
    if sum_of_its_factorial_digit == number:
        return 'STRONG!!!!'
    
    return 'Not Strong !!'