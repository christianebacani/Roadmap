# 3110.) Score of a String
# Categories : String

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        ascii_values = []
    
        for char in s:
            ascii_values.append(ord(char))
    
        total_sum = 0

        for i in range(1, len(ascii_values)):
            previous_ascii_value = ascii_values[i - 1]
            current_ascii_value = ascii_values[i]
            total_sum += abs(previous_ascii_value - current_ascii_value)

        return total_sum