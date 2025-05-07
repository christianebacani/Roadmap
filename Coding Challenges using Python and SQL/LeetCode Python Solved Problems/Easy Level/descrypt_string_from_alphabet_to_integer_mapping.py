# 1309.) Decrypt String from Alphabet to Integer Mapping
# Categories: String

class Solution:
    def freqAlphabets(self, s: str) -> str:
        digit_with_hashtag_to_char = {
            '10#': 'j', '11#': 'k', '12#': 'l',
            '13#': 'm', '14#': 'n', '15#': 'o',
            '16#': 'p', '17#': 'q', '18#': 'r',
            '19#': 's', '20#': 't', '21#': 'u',
            '22#': 'v', '23#': 'w', '24#': 'x',
            '25#': 'y', '26#': 'z'
        }
        digit_to_char = {
            '1': 'a', '2': 'b', '3': 'c',
            '4': 'd', '5': 'e', '6': 'f',
            '7': 'g', '8': 'h', '9': 'i'
        }

        digit_with_hashtags = list(digit_with_hashtag_to_char.keys())
        digits = list(digit_to_char.keys())

        for i in range(len(digit_with_hashtags)):
            s = s.replace(digit_with_hashtags[i], digit_with_hashtag_to_char[digit_with_hashtags[i]])
        
        for i in range(len(digits)):
            s = s.replace(digits[i], digit_to_char[digits[i]])
        
        return s