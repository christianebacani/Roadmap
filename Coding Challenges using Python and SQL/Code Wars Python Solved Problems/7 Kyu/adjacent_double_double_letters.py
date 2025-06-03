# Question: Adjacent Double Double Letters
# Categories: 7 Kyu

def adjacent_double_double_letters(word: str) -> bool:
    for i in range(1, len(word)):
        try:
            substring = word[i - 1] + word[i]
            adjacent_substring = word[i + 1] + word[i + 2]

            if (substring[0] == substring[1]) and (adjacent_substring[0] == adjacent_substring[1]):
                return True

        except:
            pass
    
    return False