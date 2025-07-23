# Question: Numbers to letters
# Categories: 7 Kyu

def switcher(arr: list[str]) -> str:
    numbers_to_letters_mappings = {
        '29': ' ',
        '28': '?',
        '27': '!'
    }
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(alphabets)):
        list_of_keys = list(numbers_to_letters_mappings.keys())
        
        for j in range(len(list_of_keys)):
            list_of_keys[j] = int(list_of_keys[j])
        
        numbers_to_letters_mappings[str(min(list_of_keys) - 1)] = alphabets[i]
    
    result = ''

    for i in range(len(arr)):
        result += numbers_to_letters_mappings[arr[i]]
    
    return result