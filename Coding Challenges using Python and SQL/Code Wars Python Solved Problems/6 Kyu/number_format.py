# Question: Number Format
# Categories: 6 Kyu

def number_format(number: int) -> str:
    number_string = str(number).replace('-', '')[::-1]
    formatted_number_string = ''

    for index, digit in enumerate(number_string):
        index += 1

        if index == len(number_string):
            formatted_number_string += digit
            continue

        formatted_number_string += digit
        
        if index % 3 == 0:
            formatted_number_string += ','
    
    formatted_number_string = formatted_number_string[::-1]
    
    if number < 0:
        formatted_number_string = '-' + formatted_number_string
    
    return formatted_number_string