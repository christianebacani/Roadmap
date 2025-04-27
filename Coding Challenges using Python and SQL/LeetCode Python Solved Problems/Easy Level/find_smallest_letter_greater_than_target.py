# 744.) Find Smallest Letter Greater Than Target
# Categories: Array, Binary Search

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        
        return letters[0]