# 1544.) Make The String Great
# Categories: String, Stack

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if stack == []:
                stack.append(s[i])
                continue

            if s[i].lower() != stack[-1].lower():
                stack.append(s[i])
                continue

            if (s[i].islower() and stack[-1].isupper()) or (s[i].isupper() and stack[-1].islower()):
                stack.pop(-1)
            
            else:
                stack.append(s[i])

        good_string = ''.join(stack)

        return good_string            