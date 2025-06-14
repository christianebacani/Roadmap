# Question: World Bits War
# Categories: 6 Kyu

def bits_war(numbers: list[int]) -> str:
    total_value_of_odd_bits = 0
    total_value_of_even_bits = 0

    for i in range(len(numbers)):
        binary = bin(numbers[i])[2:]
        needs_to_decrease = False

        if binary[0] == 'b':
            needs_to_decrease = True
        
        if needs_to_decrease:
            if (numbers[i] * -1) % 2 != 0:
                total_value_of_odd_bits -= (binary.count('1'))
            
            else:
                total_value_of_even_bits -= (binary.count('1'))
        
        else:
            if numbers[i] % 2 != 0:
                total_value_of_odd_bits += (binary.count('1'))

            else:
                total_value_of_even_bits += (binary.count('1'))

    if total_value_of_odd_bits == total_value_of_even_bits:
        return 'tie'
    
    elif total_value_of_odd_bits > total_value_of_even_bits:
        return 'odds win'
    
    else:
        return 'evens win'