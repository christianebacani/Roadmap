# 2108.) Find First Palindromic String in the Array
# Categories: Array, Two Pointers, String

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for i in range(len(words)):
            word = words[i]
            reverse_word = word[::-1]
        
            if word == reverse_word:
                return word

        return ""
