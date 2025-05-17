# Question: Validate the Euro bill
# Categories: Beta

def validate_euro(serial_number: str) -> bool:
    alphabets = [
        'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X',
        'Y', 'Z'
    ]
    first_letter_digits = alphabets.index(serial_number[0]) + 1
    second_letter_digits = alphabets.index(serial_number[1]) + 1

    sum_of_digits = 0

    for i in range(len(serial_number)):
        if serial_number[i].isalpha():
            continue

        sum_of_digits += int(serial_number[i])

    total = first_letter_digits + second_letter_digits + sum_of_digits

    while len(str(total)) != 1:
        result = 0

        for i in range(len(str(total))):
            result += int(str(total)[i])
        
        total = result
    
    if total == 7:
        return True
    
    return False