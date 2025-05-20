# Question: Evil Autocorrect Prank
# Categories: 6 Kyu
import re

def autocorrect(message: str) -> str:
    message = message.split()

    for i in range(len(message)):
        if message[i].lower() == 'you' or message[i].lower() == 'u':
            message[i] = 'your sister'
            continue

        if re.search(r'^yo(u{1,})[^A-Za-z]*$', message[i].lower()):
            special_characters = ''

            for j in range(len(message[i])):
                if not message[i][j].isalnum():
                    special_characters += message[i][j]

            message[i] = 'your sister' + special_characters

    return ' '.join(message)