# 557.) Reverse Words in a String III
# Categories: Two Pointers, String

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result = []
    
        for i in range(len(s)):
            reverse_word = s[i][::-1]
            result.append(reverse_word)
    
        result = ' '.join(result)

        return result