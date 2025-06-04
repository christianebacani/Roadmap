# Question: Find the number of trailing zeros, in its binary representation , of a number.
# Categories: 7 Kyu

def convert_to_binary(number: int) -> str:
    if number == 0:
        return '0'
    
    elif number == 1:
        return '1'
    
    else:
        pass

    binary = ''

    while number > 1:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    
    return binary

def trailing_zeros(n: int) -> int:
    binary_equivalent_of_n = convert_to_binary(n)[::-1]
    count = 0

    for i in range(len(binary_equivalent_of_n)):
        if binary_equivalent_of_n[i] == '1':
            break
        
        count += 1
    
    return count