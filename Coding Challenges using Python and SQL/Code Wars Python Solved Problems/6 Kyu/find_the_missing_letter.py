# Question: Find the missing letter
# Categories: 6 Kyu

def find_missing_letter(chars: str) -> str:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in range(1, len(chars)):
        previous_char = chars[i - 1]
        current_char = chars[i]

        if previous_char.isupper():
            alphabets = alphabets.upper()
        
        else:
            alphabets = alphabets.lower()

        if abs(alphabets.index(previous_char) - alphabets.index(current_char)) == 1:
            continue

        for j in range(len(alphabets)):
            if previous_char == alphabets[j]:
                return alphabets[j + 1]