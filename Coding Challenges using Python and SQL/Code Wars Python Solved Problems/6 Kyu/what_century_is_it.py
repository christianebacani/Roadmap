# Question: What century is it?
# Categories: 6 Kyu

def what_century(year: str) -> str:
    if year[:2] == '00':
        return '1st'

    if year[2:] != '00':
        century = str(int(year[:2]) + 1)

    else:
        century = str(year[:2])

    if century[0] == '1':
        return century + 'th'
    
    century_second_digits = {
        '0': '0th',
        '1': '1st',
        '2': '2nd',
        '3': '3rd',
        '4': '4th',
        '5': '5th',
        '6': '6th',
        '7': '7th',
        '8': '8th',
        '9': '9th', 
    }
    result = century[0] + century_second_digits[century[1]]
    
    return result