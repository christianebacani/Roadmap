# Question: The Hidden Word
# Categories: 7 Kyu

def hidden(num: int) -> str:
    letter_and_code = {
        'a': 6,
        'b': 1,
        'd': 7,
        'e': 4,
        'i': 3,
        'l': 2,
        'm': 9,
        'n': 8,
        'o': 0,
        't': 5
    }
    num_string = str(num)
    result = ''

    for i in range(len(num_string)):
        for letter, code in letter_and_code.items():
            if int(num_string[i]) == code:
                result += letter
                break
    
    return result