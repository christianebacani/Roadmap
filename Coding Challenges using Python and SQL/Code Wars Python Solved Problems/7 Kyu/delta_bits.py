# Question: Delta Bits
# Categories: 7 Kyu

def convert_bits(a, b):
    binary_a = bin(a)[2:]
    binary_b = bin(b)[2:]

    if len(binary_a) > len(binary_b):
        binary_b = (abs(len(binary_a) - len(binary_b)) * '0') + binary_b

    elif len(binary_b) > len(binary_a):
        binary_a = (abs(len(binary_b) - len(binary_a)) * '0') + binary_a

    else:
        pass

    total_number_of_bits = len(binary_a)
    total = 0

    for i in range(total_number_of_bits):
        if binary_a[i] != binary_b[i]:
            total += 1
    
    return total