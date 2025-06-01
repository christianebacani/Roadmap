# Question: Interlockings Binary Pairs
# Categories: 7 Kyu

def convert_to_binary(number: int) -> str:
    binary = ''

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    
    return binary

def interlockable(a: int, b: int) -> bool:
    binary_a = convert_to_binary(a)
    binary_b = convert_to_binary(b)

    if len(binary_a) > len(binary_b):
        binary_b = (len(binary_a) - len(binary_b)) * '0' + binary_b

    elif len(binary_b) > len(binary_a):
        binary_a = (len(binary_b) - len(binary_a)) * '0' + binary_a

    else:
        pass

    total_bits = len(binary_a)

    for i in range(total_bits):
        if binary_a[i] == binary_b[i] and binary_a[i] == '1':
            return False
    
    return True