# Question: Special Numbers (Special Numbers Series #5)
# Categorues: 7 Kyu

def special_number(number: int) -> str:
    if str(number) == 1 and number in range(0, 6):
        return 'Special!!'
    
    elif str(number) == 1 and number not in range(0, 6):
        return 'NOT!!'
    
    number_string = str(number)

    for i in range(len(number_string)):
        if int(number_string[i]) not in range(0, 6):
            return 'NOT!!'

    return 'Special!!'