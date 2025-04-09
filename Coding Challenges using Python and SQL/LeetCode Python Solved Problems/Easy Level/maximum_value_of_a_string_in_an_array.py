# 2496.) Maximum Value of a String in an Array
# Categories: Array, String

class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        values = []
        
        for i in range(len(strs)):
            try:
                values.append(int(strs[i]))
            
            except ValueError:
                values.append(len(strs[i]))
        
        return max(values)
            