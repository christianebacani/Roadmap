# Question: Bit Counting
# Categoties: 6 Kyu

def count_bits(n: int) -> int:
    def convert_to_binary(number: int) -> str:
        binary = ''

        while number > 0:
            remainder = number % 2
            binary = str(remainder) + binary
            number = number // 2
        
        return binary
    
    binary_equivalent = convert_to_binary(n)
        
    return binary_equivalent.count('1')