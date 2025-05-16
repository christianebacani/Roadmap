# Question: Create Phone Number
# Categories: 6 Kyu

def create_phone_number(n: list[int]) -> str:
    n = [str(num) for num in n]    
    first_three_digit = ''.join(n[:3])
    middle_three_digit = ''.join(n[3:6])
    last_four_digit = ''.join(n[6:])

    phone_number = f'({first_three_digit}) {middle_three_digit}-{last_four_digit}'

    return phone_number