# Question: Ones and Zeroes
# Categories: 7 Kyu

def same_length(binary: str) -> bool:
    if binary[0] == '0':
        return False
    
    ones, zeroes = [], []

    binary_splitted_to_ones = binary.split('0')

    for i in range(len(binary_splitted_to_ones)):
        if binary_splitted_to_ones[i] != '':
            ones.append(binary_splitted_to_ones[i])
    
    binary_splitted_to_zeroes = binary.split('1')

    for i in range(len(binary_splitted_to_zeroes)):
        if binary_splitted_to_zeroes[i] != '':
            zeroes.append(binary_splitted_to_zeroes[i])
    
    if len(ones) != len(zeroes):
        return False

    total_length = len(ones)

    for i in range(total_length):
        if len(ones[i]) != len(zeroes[i]):
            return False

    return True