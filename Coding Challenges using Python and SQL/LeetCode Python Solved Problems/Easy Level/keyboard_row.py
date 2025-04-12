# 500.) Keyboard Row
# Categories: Array, Hash Table, String

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        american_keyboard = [
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c',' v', 'b', 'n', 'm']
        ]
        answer = []

        for i in range(len(words)):
            keyboard_row_number_apperances_of_each_letter = []

            for j in range(len(words[i])):
                for k in range(len(american_keyboard)):
                    if words[i][j].lower() in american_keyboard[k]:
                        keyboard_row_number_apperances_of_each_letter.append(k)
            
            if len(set(keyboard_row_number_apperances_of_each_letter)) == 1:
                answer.append(words[i])
        
        return answer