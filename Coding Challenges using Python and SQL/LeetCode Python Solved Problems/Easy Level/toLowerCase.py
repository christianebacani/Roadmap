# 709.) To Lower Case
# Categories: String

class Solution:
    def toLowerCase(self, s: str) -> str:
        alphabet = {
        'A': 'a', 'B': 'b', 'C': 'c',
        'D': 'd', 'E': 'e', 'F': 'f',
        'G': 'g', 'H': 'h', 'I': 'i',
        'J': 'j', 'K': 'k', 'L': 'l',
        'M': 'm', 'N': 'n', 'O': 'o',
        'P': 'p', 'Q': 'q', 'R': 'r',
        'S': 's', 'T': 't', 'U': 'u',
        'V': 'v', 'W': 'w', 'X': 'x',
        'Y': 'y', 'Z': 'z'
        }
        res = ''

        for i in range(len(s)):
            if s[i] in alphabet:
                res += alphabet[s[i]]

            else:
                res += s[i]

        return res
