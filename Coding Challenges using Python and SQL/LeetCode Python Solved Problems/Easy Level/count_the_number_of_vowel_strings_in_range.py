# 2586.) Count the Number of Vowel Strings in Range
# Categories: Array, String, Counting

class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        for i in range(len(words)):
            if (words[i][0] not in vowels) or (words[i][-1] not in vowels):
                continue

            if i in range(left, right + 1):
                count += 1
        
        return count