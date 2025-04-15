# 1502.) Can Make Arithmetic Progression From Sequence
# Categories: Array, Sorting

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr = sorted(arr)
        differences_of_consecutive_elements = []

        for i in range(len(arr) - 1):
            differences_of_consecutive_elements.append(abs(arr[i] - arr[i + 1]))

        if len(set(differences_of_consecutive_elements)) == 1:
            return True
        
        return False