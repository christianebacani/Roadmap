# Question: Disarium Number (Special Numbers Series #3)
# Categories: 7 Kyu

def disarium_number(number: int) -> str:
    number_string = str(number)
    total = 0

    for index, num in enumerate(number_string):
        index += 1

        total += (int(num) ** index)
    
    if total == number:
        return 'Disarium !!'
    
    return 'Not !!'