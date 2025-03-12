# 2000.) Reverse Prefix of Word
# Categories: Two Pointers, String, Stack

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for index, char in enumerate(word):
            if char == ch:
                segment = word[:index + 1]
                reverse_segment = segment[::-1]
                word = word.replace(segment, reverse_segment)

                return word
        return word
