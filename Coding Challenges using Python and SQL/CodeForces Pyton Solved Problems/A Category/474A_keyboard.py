# 474A - Keyboard

shift = input().strip()
characters_written_by_mole = input().strip()
keyboard = [
    'qwertyuiop',
    'asdfghjkl;',
    'zxcvbnm,./'
]
original_characters = ''

for i in range(len(characters_written_by_mole)):
    for j in range(len(keyboard)):
        if characters_written_by_mole[i] not in keyboard[j]:
            continue

        target_index = keyboard[j].index(characters_written_by_mole[i])

        if shift == 'R':
            original_character = keyboard[j][target_index - 1]

        else:
            original_character = keyboard[j][target_index + 1]

        original_characters += original_character

print(original_characters)