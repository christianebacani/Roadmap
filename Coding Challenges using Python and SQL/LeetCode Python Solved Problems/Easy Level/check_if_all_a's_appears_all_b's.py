# 2124.) Check if All A's Appears Before All B's
# Categories: String

class Solution:
    def checkString(self, s: str) -> bool:
        maximum_index_of_last_appearance_of_a = 0
        index_of_first_appearance_of_b = 0
    
        for i in range(len(s)):
            if s[i] == 'a':
                maximum_index_of_last_appearance_of_a = i

        for i in range(len(s)):
            if s[i] == 'b':
                index_of_first_appearance_of_b = i
                break

        if ('b' not in s) or (maximum_index_of_last_appearance_of_a <= index_of_first_appearance_of_b):
            return True
        
        return False
        