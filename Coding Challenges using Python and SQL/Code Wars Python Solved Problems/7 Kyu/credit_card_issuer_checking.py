# Question: Credit card issuer checking
# Categories: 7 Kyu

def get_issuer(number: int) -> str:
    number_string = str(number)

    if (number_string.startswith('34') or number_string.startswith('37')) and (len(number_string) == 15):
        return 'AMEX'

    elif (number_string.startswith('6011')) and (len(number_string) == 16):
        return 'Discover'
    
    elif (number_string[:2] in ['51', '52', '53', '54', '55']) and (len(number_string) == 16):
        return 'Mastercard'
    
    elif (number_string.startswith('4')) and (len(number_string) in [13, 16]):
        return 'VISA'
    
    else:
        return 'Unknown'