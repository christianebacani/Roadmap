# Question: Converting integer to currency format
# Categories: 7 Kyu

def to_currency(price: int) -> str:
    price_string = str(price)[::-1]
    currency = ''

    for index, digit in enumerate(price_string):
        index += 1

        if index == len(price_string):
            currency += digit
            continue

        currency += digit

        if index % 3 == 0:
            currency += ','
    
    currency = currency[::-1]
    return currency