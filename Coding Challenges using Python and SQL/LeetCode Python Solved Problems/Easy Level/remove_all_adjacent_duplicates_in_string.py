# 1047.) Remove All Adjacent Duplicates In String
# Categories: String, Stack

class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []

        for i in range(len(s)):
            if result == [] or s[i] != result[-1]:
                result.append(s[i])
                continue
            
            result.pop(-1)
    
        return ''.join(result)