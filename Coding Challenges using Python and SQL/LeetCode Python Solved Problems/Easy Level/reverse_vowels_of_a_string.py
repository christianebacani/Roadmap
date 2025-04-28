# 345.) Reverse Vowels of a String
# Categories: Two Pointers

class Solution:
    def reverseVowels(self, s: str) -> str:
        original_vowels = []
        reversed_vowels = []

        for i in range(len(s)):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                original_vowels.append(s[i])
        
        for i in range(len(original_vowels[::-1])):
            reversed_vowels.append(original_vowels[::-1][i])

        lst_s = list(s)

        for i in range(len(lst_s)):
            if lst_s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                target_index = original_vowels.index(lst_s[i])
                lst_s[i] = reversed_vowels[target_index]

                original_vowels.pop(target_index)
                reversed_vowels.pop(target_index)

        s = ''.join(lst_s)
        return s