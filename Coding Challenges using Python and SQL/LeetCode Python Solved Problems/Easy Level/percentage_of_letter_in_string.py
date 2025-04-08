# 2278.) Percentage of Letter in String
# Categories: String

import math

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        frequency = s.count(letter)
        
        if frequency == 0:
            return 0
        
        percentage = math.floor((frequency / len(s)) * 100)

        return percentage