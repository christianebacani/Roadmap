# Question: Colorful Number
# Categories: 6 Kyu

def colorful(number: int) -> bool:
    list_of_digits = []
    string_number = str(number)

    for i in range(len(string_number)):
        list_of_digits.append(int(string_number[i]))
    
    if len(string_number) > 1:
        for i in range(1, len(string_number)):
            list_of_digits.append(int(string_number[i - 1]) * int(string_number[i]))
    
    if len(string_number) > 2:
        total_product = 1

        for i in range(len(string_number)):
            total_product *= int(string_number[i])
        
        list_of_digits.append(total_product)
    
    return len(list_of_digits) == len(set(list_of_digits))