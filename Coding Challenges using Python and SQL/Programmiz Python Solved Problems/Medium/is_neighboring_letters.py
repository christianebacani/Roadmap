# Question: Write a function to check if all the letters in a given string are neighboring letters in the alphabet
# Categories: Medium

def check_neighboring_letters(s : str) -> bool:
    alphabets = [
        'a', 'b', 'c', 'd',
        'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p',
        'q', 'r', 's', 't',
        'u', 'v', 'w', 'x',
        'y', 'z'
    ]

    for i in range(1, len(s)):
        previous_char = s[i - 1]
        char = s[i]

        if abs(alphabets.index(previous_char) - alphabets.index(char)) != 1:
            return False
    
    return True