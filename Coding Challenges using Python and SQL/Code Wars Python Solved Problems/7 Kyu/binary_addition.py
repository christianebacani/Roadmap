# Question: Binary Addition
# Categories: 7 Kyu

def add_binary(a: int, b: int) -> str:
    def convert_to_binary(number: int) -> str:
        binary = ''

        while number > 0:
            remainder = number % 2
            binary = str(remainder) + binary
            number = number // 2
        
        return binary
    
    return convert_to_binary(a + b)