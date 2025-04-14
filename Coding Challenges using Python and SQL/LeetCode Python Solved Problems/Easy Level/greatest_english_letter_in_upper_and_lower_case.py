# 2309.) Greatest English Letter in Upper and Lower Case
# Categories: Hash Table, String, Enumeration

class Solution:
    def greatestLetter(self, s: str) -> str:
        alphabets = [
            'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z'
        ]
        greatest_letters = []

        for i in range(len(alphabets)):
            letter_occurences = []

            for j in range(len(s)):
                if alphabets[i] == s[j].lower():
                    letter_occurences.append(s[j])
            
            if len(set(letter_occurences)) != 2:
                continue

            if alphabets[i].upper() not in greatest_letters:
                greatest_letters.append(alphabets[i].upper())
    
        if greatest_letters == []:
            return ''
        
        greatest_letters = sorted(greatest_letters, reverse=True)
        return greatest_letters[0]