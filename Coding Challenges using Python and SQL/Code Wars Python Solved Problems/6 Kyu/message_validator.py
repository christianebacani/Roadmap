# Question: Message Validator
# Categories: 6 Kyu

def get_length_of_every_words(word: str) -> list[int]:
    result = ''

    for i in range(len(word)):
        if word[i].isdigit():
            result += word[i]

        else:
            result += ' '
    
    result = result.split()

    for i in range(len(result)):
        result[i] = int(result[i])
    
    return result

def get_every_words(message: str) -> list[str]:
    result = ''

    for i in range(len(message)):
        if message[i].isalpha():
            result += message[i]
        
        else:
            result += ' '
    
    result = result.split()

    return result

def is_a_valid_message(message: str) -> bool:
    if message == '':
        return True
    
    if message[-1].isdigit():
        return False

    length_of_every_words = get_length_of_every_words(message)
    words = get_every_words(message)

    if len(length_of_every_words) != len(words):
        return False

    total_length = len(words)

    for i in range(total_length):
        if len(words[i]) != length_of_every_words[i]:
            return False
    
    return True