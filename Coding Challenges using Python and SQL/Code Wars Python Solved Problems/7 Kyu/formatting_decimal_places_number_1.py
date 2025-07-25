# Question: Formatting decimal places #1
# Categories: 7 Kyu

def two_decimal_places(number: float) -> float:
    whole_number = str(number).split('.')[0]
    decimal = str(number).split('.')[1][:2]
    result = float(whole_number + '.' + decimal)

    return result