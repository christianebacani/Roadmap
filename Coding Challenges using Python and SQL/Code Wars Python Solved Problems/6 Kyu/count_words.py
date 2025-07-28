# Question: Count words
# Categories: 6 Kyu

def word_count(s: str) -> int:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    new_s = ''

    for i in range(len(s)):
        if s[i].lower() in alphabets:
            new_s += s[i]

        else:
            new_s += ' '
    
    s = new_s
    s = s.split()
    
    excluded_words = ['a', 'the', 'on', 'at', 'of', 'upon', 'in', 'as']
    total = 0

    for i in range(len(s)):
        s[i] = str(s[i]).lower()

        if s[i] in excluded_words:
            continue
        
        total += 1

    return total