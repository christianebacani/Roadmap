# 3019.) Number of Changing Keys
# Categories: String

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = list(s.lower())
        number_of_key_changes = 0
        
        for i in range(1, len(s)):
            previous_key = s[i - 1]
            current_key = s[i]

            if current_key != previous_key:
                number_of_key_changes += 1

        return number_of_key_changes
