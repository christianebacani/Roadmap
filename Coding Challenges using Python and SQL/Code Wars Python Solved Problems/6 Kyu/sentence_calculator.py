# Question: Sentence Calculator
# Categories: 6 Kyu

def letters_to_numbers(s: str) -> int:
    lower_case_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    upper_case_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0

    for i in range(len(s)):
        if not s[i].isalnum():
            continue

        if s[i] in lower_case_alphabets:
            total += (lower_case_alphabets.index(s[i]) + 1)
        
        elif s[i] in upper_case_alphabets:
            total += ((upper_case_alphabets.index(s[i]) + 1) * 2)
        
        else:
            total += int(s[i])

    return total