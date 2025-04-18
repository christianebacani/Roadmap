# 3120.) Count the Number of Special Characters I
# Categories: Hash Table, String

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        distinct_chars = list(set(word))
        special_characters = []

        for i in range(len(distinct_chars)):
            common_char = [distinct_chars[i]]

            for j in range(len(distinct_chars)):
                if common_char[-1] == distinct_chars[j]:
                    continue

                if common_char[-1].lower() == distinct_chars[j].lower():
                    common_char.append(distinct_chars[j])
            
            if len(common_char) != 2:
                continue

            if common_char[-1].lower() not in special_characters:
                special_characters.append(common_char[-1].lower())
            
        return len(special_characters)