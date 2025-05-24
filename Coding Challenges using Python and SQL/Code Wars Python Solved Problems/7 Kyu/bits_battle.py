# Question: Bits Battle
# Categories: 7 Kyu

def bits_battle(numbers: list[int]) -> str:
    def convert_to_binary(number: int) -> str:
        binary = ''

        while number > 0:
            remainder = number % 2
            binary = str(remainder) + binary
            number = number // 2
        
        return binary
    
    number_of_zeroes = 0
    number_of_ones = 0

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            number_of_zeroes += convert_to_binary(numbers[i]).count('0')
        
        else:
            number_of_ones += convert_to_binary(numbers[i]).count('1')
    
    if number_of_zeroes > number_of_ones:
        return 'evens win'

    elif number_of_ones > number_of_zeroes:
        return 'odds win'
    
    else:
        return 'tie'