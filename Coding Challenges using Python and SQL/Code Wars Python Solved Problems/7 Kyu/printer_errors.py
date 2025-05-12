# Question: Printer Errors
# Categories: 7 Kyu

def printer_error(s: str):
    good_control_string = [
        'a', 'b', 'c', 'd', 'e',
        'f', 'g', 'h', 'i', 'j',
        'k', 'l' ,'m'
    ]
    number_of_bad_control_string = 0

    for i in range(len(s)):
        if s[i] not in good_control_string:
            number_of_bad_control_string += 1
    
    return f'{number_of_bad_control_string}/{len(s)}'