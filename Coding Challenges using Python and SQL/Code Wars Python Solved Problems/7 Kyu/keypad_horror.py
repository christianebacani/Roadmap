# Question: Keypad horror
# Categories: 7 Kyu

def computer_to_phone(numbers: str) -> str:
    computer_to_phone_keypad = {
        '7': '1', '8': '2', '9': '3',
        '4': '4', '5': '5', '6': '6',
        '1': '7', '2': '8', '3': '9',
        '0': '0'
    }
    result = ''

    for i in range(len(numbers)):
        result += computer_to_phone_keypad[numbers[i]]

    return result