# 2710.) Remove Trailing Zeros From a String
# Categories: String

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        reverse_num = num[::-1]

        for digit in reverse_num:
            if digit == '0':
                reverse_num = reverse_num.removeprefix('0')
            
            else:
                break
        
        return reverse_num[::-1]
