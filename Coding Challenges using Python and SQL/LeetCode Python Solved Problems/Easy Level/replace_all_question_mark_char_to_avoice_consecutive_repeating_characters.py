# 1576.) Replace All ?'s to Avoid Consecutive Repeating Characters
# Categories: String

class Solution:
    def modifyString(self, s: str) -> str:
        alphabets = [
            'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z'
        ]

        lst_s = list(s)

        for i in range(len(lst_s)):
            if lst_s[i] != '?':
                continue
            
            if i - 1 < 0:
                previous_character = ''
            
            else:
                previous_character = lst_s[i - 1]
            
            if (i + 1) > len(lst_s) - 1:
                next_character = ''
            
            else:
                next_character = lst_s[i + 1]

            for j in range(len(alphabets)):
                if alphabets[j] != previous_character and alphabets[j] != next_character:
                    lst_s[i] = alphabets[j]
                    break

        s = ''.join(lst_s)

        return s