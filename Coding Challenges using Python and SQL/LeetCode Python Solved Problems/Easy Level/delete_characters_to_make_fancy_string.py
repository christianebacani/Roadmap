# 1957.) Delete Characters to Make Fancy String
# Categories: String

class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ''

        for i in range(len(s)):
            try:
                if s[i] == s[i + 1] == s[i + 2]:
                    continue
                
                else:
                    result += s[i]

            except IndexError:
                result += s[i]
                
        return result