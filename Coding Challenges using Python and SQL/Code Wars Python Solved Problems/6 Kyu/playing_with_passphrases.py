# Question: Playing with passphrases
# Categories: 6 Kyu

def shift_each_letter(word: str, number_of_shift: int) -> str:
    letter = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for i in range(len(word)):
        if not word[i].isalpha():
            result += word[i]
            continue

        if word[i].isupper():
            letter = letter.upper()
        
        else:
            letter = letter.lower()

        target_index = letter.index(word[i]) + number_of_shift

        if target_index <= 25:
            result += letter[target_index]
            continue

        if target_index % 25 == 0:
            target_index = letter.index(word[i]) - 1
            result += letter[target_index]

        else:
            target_index = (target_index % 25) - 1
            result += letter[target_index]

    return result

def replace_each_digit_by_nine_complement(word: str) -> str:
    complement = {
        '0': '9',
        '1': '8',
        '2': '7',
        '3': '6',
        '4': '5',
        '5': '4',
        '6': '3',
        '7': '2',
        '8': '1',
        '9': '0'
    }
    result = ''

    for i in range(len(word)):
        if not word[i].isdigit():
            result += word[i]
            continue
        
        result += complement[word[i]]
    
    return result

def upcase_and_downcase_per_index_position(word: str) -> str:
    word = list(word)

    for i in range(len(word)):
        if i % 2 == 0:
            word[i] = word[i].upper()
        
        else:
            word[i] = word[i].lower()
    
    return ''.join(word)

def reverse_word(word: str) -> str:
    return word[::-1]

def play_pass(s: str, shift: int) -> str:
    s = shift_each_letter(s, shift)
    s = replace_each_digit_by_nine_complement(s)
    s = upcase_and_downcase_per_index_position(s)
    s = reverse_word(s)
    return s