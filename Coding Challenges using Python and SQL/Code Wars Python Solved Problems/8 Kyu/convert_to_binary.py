# Question: Convert to Binary
# Cateogies: 8 Kyu

def convert_to_binary(number: int) -> str:
    if number == 0:
        return '0'

    binary = ''

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    
    return binary

def to_binary(b: int) -> int:
    binary_b = convert_to_binary(b)
    d = int(binary_b)
    return d